import type { APIRoute } from 'astro';
import { ANTHROPIC_API_KEY } from 'astro:env/server';
import Anthropic from '@anthropic-ai/sdk';
import { SYSTEM_PROMPT } from '../../lib/chat-context';

export const prerender = false;

const MODEL = 'claude-opus-5';
// Public endpoint: hard caps keep a single visitor from running up the bill.
const MAX_TOKENS = 1024;
const MAX_TURNS = 20;
const MAX_CHARS = 1000;
const RATE_LIMIT = 20;
const RATE_WINDOW_MS = 10 * 60 * 1000;

const client = new Anthropic({ apiKey: ANTHROPIC_API_KEY });

// Best effort only: serverless instances don't share memory, so this limits bursts
// per instance. The real ceiling is the spend limit set in the Anthropic Console.
const hits = new Map<string, number[]>();

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  if (hits.size > 5000) hits.clear();
  const recent = (hits.get(ip) ?? []).filter((t) => now - t < RATE_WINDOW_MS);
  recent.push(now);
  hits.set(ip, recent);
  return recent.length > RATE_LIMIT;
}

function parseMessages(body: unknown): Anthropic.Beta.BetaMessageParam[] | null {
  const raw = (body as { messages?: unknown })?.messages;
  if (!Array.isArray(raw) || raw.length === 0 || raw.length > MAX_TURNS) return null;

  const messages: Anthropic.Beta.BetaMessageParam[] = [];
  for (const [i, m] of raw.entries()) {
    const expectedRole = i % 2 === 0 ? 'user' : 'assistant';
    if (m?.role !== expectedRole || typeof m.content !== 'string') return null;
    const content = m.content.trim();
    if (!content || content.length > MAX_CHARS * (expectedRole === 'assistant' ? 8 : 1)) return null;
    messages.push({ role: expectedRole, content });
  }
  return messages.at(-1)?.role === 'user' ? messages : null;
}

const json = (status: number, error: string) =>
  new Response(JSON.stringify({ error }), { status, headers: { 'Content-Type': 'application/json' } });

export const POST: APIRoute = async ({ request, clientAddress }) => {
  if (isRateLimited(clientAddress)) {
    return json(429, 'Too many messages. Please try again in a few minutes.');
  }

  const messages = parseMessages(await request.json().catch(() => null));
  if (!messages) return json(400, 'Invalid message.');

  const stream = client.beta.messages.stream({
    model: MODEL,
    max_tokens: MAX_TOKENS,
    output_config: { effort: 'low' },
    // If a safety classifier declines, the API retries on its recommended fallback model.
    betas: ['server-side-fallback-2026-07-01'],
    fallbacks: 'default',
    system: [{ type: 'text', text: SYSTEM_PROMPT, cache_control: { type: 'ephemeral' } }],
    messages,
  });

  const encoder = new TextEncoder();
  const body = new ReadableStream<Uint8Array>({
    async start(controller) {
      try {
        for await (const event of stream) {
          if (event.type === 'content_block_delta' && event.delta.type === 'text_delta') {
            controller.enqueue(encoder.encode(event.delta.text));
          }
        }
        const final = await stream.finalMessage();
        if (final.stop_reason === 'refusal') {
          controller.enqueue(encoder.encode("Sorry, I can't help with that. Ask me about Walter's work instead."));
        }
      } catch (err) {
        console.error('chat stream failed', err);
        controller.enqueue(encoder.encode('\n\nSomething went wrong. Please try again later.'));
      } finally {
        controller.close();
      }
    },
    cancel() {
      stream.abort();
    },
  });

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' },
  });
};
