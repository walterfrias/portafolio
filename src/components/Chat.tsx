import { useEffect, useRef, useState } from 'react';

type Message = { role: 'user' | 'assistant'; content: string };

const SUGGESTIONS = [
  'What has Walter built?',
  'Is he available for freelance work?',
  '¿Qué experiencia tiene en Web3?',
];

// Keep in sync with MAX_TURNS in src/pages/api/chat.ts (must be odd so history starts with a user turn).
const MAX_HISTORY = 19;

export default function Chat() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const listRef = useRef<HTMLDivElement>(null);
  const toggleRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (open) inputRef.current?.focus();
  }, [open]);

  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight });
  }, [messages]);

  function close() {
    setOpen(false);
    toggleRef.current?.focus();
  }

  async function send(text: string) {
    const content = text.trim();
    if (!content || loading) return;

    const history = [...messages, { role: 'user' as const, content }];
    setMessages([...history, { role: 'assistant', content: '' }]);
    setInput('');
    setLoading(true);

    const appendToReply = (chunk: string) =>
      setMessages((prev) => {
        const last = prev[prev.length - 1];
        return [...prev.slice(0, -1), { ...last, content: last.content + chunk }];
      });

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history.slice(-MAX_HISTORY) }),
      });

      if (!res.ok || !res.body) {
        const data = await res.json().catch(() => null);
        appendToReply(data?.error ?? 'Something went wrong. Please try again later.');
        return;
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        appendToReply(decoder.decode(value, { stream: true }));
      }
    } catch {
      appendToReply('Network error. Please check your connection and try again.');
    } finally {
      // The API rejects empty turns, so never keep one in the history.
      setMessages((prev) => {
        const last = prev[prev.length - 1];
        return last.content ? prev : [...prev.slice(0, -1), { ...last, content: 'No response. Please try again.' }];
      });
      setLoading(false);
      inputRef.current?.focus();
    }
  }

  return (
    <>
      <button
        ref={toggleRef}
        type="button"
        onClick={() => (open ? close() : setOpen(true))}
        aria-expanded={open}
        aria-controls="portfolio-chat"
        className="fixed bottom-5 right-5 z-50 flex items-center gap-2 rounded-full border border-amber-300/40 bg-slate-900 px-5 py-3 text-xs font-semibold uppercase tracking-widest text-amber-300 shadow-lg shadow-black/40 transition-colors duration-200 hover:border-amber-300 hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-amber-300 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950"
      >
        {open ? (
          'Close'
        ) : (
          <>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
            </svg>
            Ask about me
          </>
        )}
      </button>

      {open && (
        <div
          id="portfolio-chat"
          role="dialog"
          aria-label="Chat about Walter"
          onKeyDown={(e) => e.key === 'Escape' && close()}
          className="fixed bottom-20 right-5 z-50 flex h-[min(32rem,calc(100dvh-7rem))] w-[calc(100vw-2.5rem)] max-w-sm flex-col overflow-hidden rounded-xl border border-slate-700 bg-slate-950 shadow-2xl shadow-black/60"
        >
          <div className="border-b border-slate-800 px-4 py-3">
            <p className="text-sm font-semibold text-white">Ask about Walter</p>
            <p className="text-xs text-slate-400">AI assistant · answers may contain mistakes</p>
          </div>

          <div ref={listRef} aria-live="polite" className="flex-1 space-y-3 overflow-y-auto px-4 py-4">
            {messages.length === 0 && (
              <div className="flex flex-col gap-2">
                <p className="mb-1 text-sm text-slate-300">
                  Hi! Ask me about Walter's projects, skills or availability.
                </p>
                {SUGGESTIONS.map((s) => (
                  <button
                    key={s}
                    type="button"
                    onClick={() => send(s)}
                    className="w-fit rounded-full border border-teal-500/40 px-3 py-1.5 text-left text-xs text-teal-400 transition-colors duration-200 hover:border-teal-400 hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-amber-300"
                  >
                    {s}
                  </button>
                ))}
              </div>
            )}

            {messages.map((m, i) => (
              <div
                key={i}
                className={`max-w-[85%] whitespace-pre-wrap break-words rounded-lg px-3 py-2 text-sm leading-relaxed ${
                  m.role === 'user' ? 'ml-auto bg-amber-300/10 text-white' : 'bg-slate-800/60 text-slate-200'
                }`}
              >
                {m.content || <span className="text-slate-400">Thinking…</span>}
              </div>
            ))}
          </div>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              send(input);
            }}
            className="flex items-end gap-2 border-t border-slate-800 p-3"
          >
            <label htmlFor="chat-input" className="sr-only">
              Your question
            </label>
            <textarea
              id="chat-input"
              ref={inputRef}
              rows={1}
              maxLength={1000}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  send(input);
                }
              }}
              placeholder="Type a question…"
              className="max-h-28 flex-1 resize-none rounded-lg border border-slate-700 bg-slate-900 px-3 py-2 text-sm text-white placeholder:text-slate-500 focus:border-amber-300/60 focus:outline-none"
            />
            <button
              type="submit"
              disabled={loading || !input.trim()}
              aria-label="Send"
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-amber-300 text-slate-950 transition-opacity duration-200 hover:bg-amber-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-amber-300 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-950 disabled:opacity-40"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <line x1="22" y1="2" x2="11" y2="13" />
                <polygon points="22 2 15 22 11 13 2 9 22 2" />
              </svg>
            </button>
          </form>
        </div>
      )}
    </>
  );
}
