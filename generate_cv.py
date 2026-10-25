import sys
from pathlib import Path

from fpdf import FPDF, XPos, YPos

# Default: public version served from the website, without phone number.
# `--send`: version to send directly to recruiters, with phone (from cv_envio/telefono.txt),
# saved in cv_envio/ (gitignored).
SEND = "--send" in sys.argv

LM = 17   # left margin
RM = 17   # right margin
PW = 210  # A4 width
TW = PW - LM - RM  # text width = 176


class CV(FPDF):
    def reset_x(self):
        self.set_x(LM)

    def section_title(self, title):
        self.ln(5)
        self.reset_x()
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(30, 30, 30)
        self.cell(TW, 6, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(180, 180, 180)
        self.line(LM, self.get_y(), PW - RM, self.get_y())
        self.ln(3)

    def row(self, text, size=9, bold=False, indent=0, color=(50, 50, 50)):
        self.set_font("Helvetica", "B" if bold else "", size)
        self.set_text_color(*color)
        self.set_x(LM + indent)
        self.multi_cell(TW - indent, 5, text)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(50, 50, 50)
        self.set_x(LM + 4)
        self.multi_cell(TW - 4, 5, f"-  {text}")


pdf = CV(format="A4")
pdf.add_page()
pdf.set_margins(LM, 15, RM)
pdf.set_auto_page_break(auto=True, margin=15)

# ── NAME ──────────────────────────────────────────────────────
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(20, 20, 20)
pdf.set_x(LM)
pdf.cell(TW, 10, "Walter Frias", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(80, 80, 80)
pdf.set_x(LM)
pdf.cell(TW, 5, "Product Engineer  |  Applied AI  |  10+ years in operations", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

# ── CONTACT ───────────────────────────────────────────────────
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(50, 50, 50)
pdf.set_x(LM)
contact = "Buenos Aires, Argentina   |   walter.frias.dev@gmail.com"
if SEND:
    # The phone lives in a gitignored file so it never reaches the public repo.
    phone = (Path(__file__).parent / "cv_envio" / "telefono.txt").read_text().strip()
    contact += f"   |   {phone}"
pdf.cell(TW, 5, contact,
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_text_color(0, 80, 180)
pdf.set_x(LM)
pdf.cell(TW, 5, "walterfrias.dev   |   github.com/walterfrias   |   linkedin.com/in/walter-frias-61b03244",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# ── SUMMARY ───────────────────────────────────────────────────
pdf.section_title("Summary")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(50, 50, 50)
pdf.set_x(LM)
pdf.multi_cell(TW, 5,
    "Product Engineer with 10+ years managing a business in Buenos Aires. I find real operational "
    "problems and build the software that solves them, end to end: Django and React web apps, "
    "React Native mobile, applied AI with the Claude API, and self-hosted services running 24/7. "
    "My systems run in production with real users and real money: a restaurant management SaaS "
    "used daily by 10 users across 2 restaurants, saving an estimated 40+ hours of manual work per month, "
    "and two trading bots I built and operate."
)

# ── PROJECTS ──────────────────────────────────────────────────
pdf.section_title("Projects")

projects = [
    {
        "title": "Comanda - Restaurant Management SaaS (In Production, 2026 - Present)",
        "stack": "Python / Django REST Framework / PostgreSQL / React / TypeScript / PWA / React Native / Expo / Claude API",
        "bullets": [
            "In daily production use by 10 users across 2 restaurants since mid-2026, saving an estimated 40+ hours "
            "per month of manual Excel work across purchasing, management and kitchen staff.",
            "Multi-tenant from day one: the second restaurant was onboarded on the same platform. "
            "Managers check the business numbers in real time from their phones.",
            "Recipe costs and margins recalculate automatically when supplier prices change, across 8 unit types.",
            "Stock counts, supplier orders via WhatsApp, daily cash and monthly cost reports, 7 role-based views.",
            "In development: mobile app with AI invoice reading (Claude vision + structured outputs), "
            "reviewed by the manager before anything is saved.",
        ],
        "url": "https://www.comanda.com.ar/",
    },
    {
        "title": "Automated Trading Bots - Hyperliquid (Live 24/7 since April 2026)",
        "stack": "Python / asyncio / Hyperliquid SDK / systemd / Ubuntu Server / Telegram Bot API",
        "bullets": [
            "Built and operate two bots trading real capital 24/7 on a self-hosted Ubuntu server, "
            "with systemd auto-restart and Telegram status alerts.",
            "HL-Delta runs a delta-neutral funding-rate strategy with automatic coin rotation; "
            "HL-Spot trades BTC on a backtested signal with partial take-profits.",
            "Wrote the postmortem of a production incident (a silent order failure that led to a liquidation) "
            "and shipped the fixes: every order is now validated before the next action.",
        ],
        "url": None,
    },
    {
        "title": "CooperaApp - Transparency for School Cooperatives (Launching 2027)",
        "stack": "Django REST Framework / React / TypeScript / Vite / PostgreSQL / Docker / Solidity",
        "bullets": [
            "Born from my term as cooperative president: parents distrusted how dues and funds were handled, "
            "because that information never left the cooperative.",
            "Gives every family visibility into paid dues, funds raised and school news; multi-tenant with 6-role RBAC.",
            "Launching without blockchain, since parents don't need a DAO to trust the numbers; a DAO-per-school "
            "version with its own ERC-20 token is built on Base Sepolia (testnet) for a later scale-up.",
        ],
        "url": "https://cooperadora-escuela-27.vercel.app/",
    },
]

for p in projects:
    pdf.reset_x()
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(20, 20, 20)
    pdf.set_x(LM)
    pdf.cell(TW, 5, p["title"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 100, 100)
    pdf.set_x(LM)
    pdf.cell(TW, 4, p["stack"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    for b in p["bullets"]:
        pdf.bullet(b)

    if p["url"]:
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(0, 80, 180)
        pdf.set_x(LM + 4)
        pdf.cell(TW - 4, 4, p["url"], new_x=XPos.LMARGIN, new_y=YPos.NEXT, link=p["url"])
        pdf.set_text_color(50, 50, 50)
    pdf.ln(2)

# ── OTHER WORK ────────────────────────────────────────────────
pdf.section_title("Other Work")
other = [
    ("DAO - Ethereum Hackathon, 1st place ETH KIPU Latam 2024", "Solidity, Hardhat, Next.js",
     "https://hackatonbuildingdao.vercel.app/"),
    ("ERC-20 Token Swap Pool", "Solidity, React, Wagmi",
     "https://swaperc20.netlify.app/"),
    ("Project Management System", "Angular, NestJS, PostgreSQL, Docker",
     "https://integrador-des-app-web.vercel.app/"),
    ("Portfolio with AI chat assistant", "Astro, React, Claude API",
     "https://walterfrias.dev"),
]
for title, stack, url in other:
    pdf.set_x(LM)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(20, 20, 20)
    pdf.write(5, title)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 100, 100)
    pdf.write(5, f"  ({stack})  ")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(0, 80, 180)
    pdf.write(5, url.removeprefix("https://").rstrip("/"), link=url)
    pdf.ln(5)
pdf.set_text_color(50, 50, 50)

# ── EXPERIENCE ────────────────────────────────────────────────
# Keep the experience section together instead of splitting it at the page bottom.
if pdf.get_y() > 230:
    pdf.add_page()
pdf.section_title("Professional Experience")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(20, 20, 20)
pdf.set_x(LM)
pdf.cell(TW, 5, "General Manager  |  Private Business, Buenos Aires  |  2016 - Present",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.bullet("Lead a team of up to 10 people in daily operations.")
pdf.bullet("Own cost control, supplier management and daily cash: the operational knowledge behind the software I build.")
pdf.bullet("Resolve high-pressure situations and coordinate across teams and suppliers.")
pdf.ln(2)

pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(20, 20, 20)
pdf.set_x(LM)
pdf.cell(TW, 5, "President  |  School Cooperative  |  2025",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.bullet("Managed the cooperative's dues, funds and communication with families.")
pdf.bullet("Identified the trust problem around how funds were reported, which led to building CooperaApp.")

# ── SKILLS ────────────────────────────────────────────────────
pdf.section_title("Skills")
skills = [
    ("Applied AI",       "Claude API (vision, structured outputs, streaming, prompt caching), MCP servers, "
                         "AI-assisted development (Claude Code)"),
    ("Product & Ops",    "Product discovery, process design, team leadership, cost control, end-to-end ownership"),
    ("Stack",            "Python, Django, TypeScript, React, Next.js, React Native / Expo, Angular, "
                         "Node.js (Express, NestJS), PostgreSQL, Docker, Linux, Ubuntu Server"),
    ("Blockchain",       "Solidity, Hardhat, Wagmi, ERC-20 / ERC-721"),
    ("Also worked with", "Flask, MySQL, Firebase, Vite, Tailwind CSS"),
]
COL = 40
for label, value in skills:
    y = pdf.get_y()
    # label
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(LM, y)
    pdf.cell(COL, 5, f"{label}:", new_x=XPos.RIGHT, new_y=YPos.TOP)
    # value
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.set_xy(LM + COL, y)
    pdf.multi_cell(TW - COL, 5, value)


# ── EDUCATION ─────────────────────────────────────────────────
pdf.section_title("Education & Certifications")

edu = [
    ("Universidad Nacional de Entre Rios (UNER)",
     "Tecnicatura Universitaria en Desarrollo Web (Web Development degree)  |  2024 - 2026"),
    ("ETH KIPU Latam",
     "Ethereum Developer Pack  |  2024  -  on-chain certificate"),
    ("Talento Tech - Buenos Aires Ministry of Education",
     "Node.js & React.js  |  2025  -  certified"),
    ("Codo a Codo - Buenos Aires Ministry of Education",
     "Full Stack Python + Django specialization  |  2022-2023  -  certified"),
    ("ISFA Manuel Belgrano",
     "National Teaching Degree in Visual Arts  |  2018-2024"),
    ("ProCp",
     "Ontological Leadership Coaching  |  2018"),
]

for inst, detail in edu:
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(LM)
    pdf.cell(TW, 5, inst, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(LM + 4)
    pdf.cell(TW - 4, 4, detail, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

# ── LANGUAGES ─────────────────────────────────────────────────
pdf.section_title("Languages")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(50, 50, 50)
pdf.set_x(LM)
pdf.cell(TW, 5,
         "Spanish - Native     |     English - Intermediate (actively improving with formal classes)",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

out_dir = Path("/home/xtsulyts/Escritorio/portafolio") / ("cv_envio" if SEND else "")
out_dir.mkdir(exist_ok=True)
out = out_dir / "Walter_Frias_CV_2026.pdf"
pdf.output(str(out))
print(f"CV generado: {out}")
