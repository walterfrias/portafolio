from fpdf import FPDF, XPos, YPos

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
pdf.cell(TW, 5, "Full Stack Developer  |  Web3", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(2)

# ── CONTACT ───────────────────────────────────────────────────
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(50, 50, 50)
pdf.set_x(LM)
pdf.cell(TW, 5, "Buenos Aires, Argentina   |   walter.frias.dev@gmail.com   |   +54 9 11 3486 3363",
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
    "Full Stack Developer specialized in web and Web3 applications, with hands-on experience "
    "across the complete development cycle. I build scalable backend architectures, robust APIs, "
    "and dynamic frontends. I have applied these skills in blockchain environments, developing "
    "and integrating smart contracts with complex business logic connected to frontend "
    "applications. Background in visual arts and 9+ years of team leadership bring a unique "
    "perspective to product and design decisions."
)

# ── SKILLS ────────────────────────────────────────────────────
pdf.section_title("Technical Skills")
skills = [
    ("Languages",   "Python, JavaScript, TypeScript"),
    ("Frontend",    "React, Next.js, Vite.js, Angular, Astro, Tailwind CSS, HTML, CSS"),
    ("Backend",     "Django, Flask, Node.js, Express.js, NestJS"),
    ("Blockchain",  "Solidity, Hardhat, Scaffold-ETH, Viem, Wagmi, ERC20 / ERC721"),
    ("Databases",   "PostgreSQL, MySQL, Firebase"),
    ("DevOps & OS", "Docker, Linux (shell scripting), Git / GitHub"),
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

# ── PROJECTS ──────────────────────────────────────────────────
pdf.section_title("Projects")

projects = [
    {
        "title": "DAO - Ethereum Hackathon (1st Place)",
        "stack": "Solidity / Hardhat / Scaffold-ETH / Next.js / TypeScript",
        "bullets": [
            "Won 1st place at ETH KIPU Latam 2024 hackathon building a consortium management DAO.",
            "Implemented on-chain voting, proposal creation and fund management contracts in Solidity.",
        ],
        "url": "https://hackatonbuildingdao.vercel.app/",
    },
    {
        "title": "CooperaApp - SaaS for School Cooperatives",
        "stack": "Django REST Framework / React / TypeScript / Vite / PostgreSQL / Docker / Solidity",
        "bullets": [
            "Built a multi-tenant SaaS platform for Argentine school cooperatives with 6-role RBAC, subscription lifecycle management and path-based tenant routing.",
            "Integrated a Solidity Factory contract (Base Sepolia) that deploys an individual DAO with its own ERC-20 COOP token per school; token minted automatically on each payment.",
        ],
        "url": "https://cooperadora-escuela-27.vercel.app/",
    },
    {
        "title": "Project Management System - Fullstack",
        "stack": "Angular / NestJS / TypeScript / PostgreSQL / Docker",
        "bullets": [
            "Built a fullstack project management app with role-based access (Admin/Operator), Kanban board, advanced filtering, pagination and CSV export.",
            "Designed REST API with NestJS covering projects, clients, tasks and user assignments; containerized with Docker.",
        ],
        "url": "https://integrador-des-app-web.vercel.app/",
    },
    {
        "title": "ERC-20 Token Swap Pool",
        "stack": "Solidity / Hardhat / TypeScript / React / Vite / Tailwind / Wagmi",
        "bullets": [
            "Implemented ERC-20 liquidity pool with deposit, withdrawal and swap logic in Solidity from scratch.",
            "Connected on-chain contract calls to a React frontend via Wagmi; deployed on Sepolia testnet.",
        ],
        "url": "https://swaperc20.netlify.app/",
    },
    {
        "title": "Financial Dashboard App - Fullstack",
        "stack": "Python / Django / Docker / Next.js / TypeScript / React / PostgreSQL",
        "bullets": [
            "Built a fullstack financial management app with transaction tracking, interactive charts and PDF report exports.",
            "Dockerized frontend and backend as independent services; production images published on Docker Hub.",
        ],
        "url": "https://django-dashboard-financial.vercel.app/",
    },
    {
        "title": "E-Commerce Platform (B2C)",
        "stack": "Node.js / Express / Firebase / JavaScript / React / Vite / Tailwind",
        "bullets": [
            "Developed a complete B2C e-commerce platform with product catalog, shopping cart and checkout flow.",
            "Built a decoupled REST API with Node.js and Express, persisted with Firebase, deployed on Render.",
        ],
        "url": "https://eshopdevices.netlify.app/",
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

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(0, 80, 180)
    pdf.set_x(LM + 4)
    pdf.cell(TW - 4, 4, p["url"], new_x=XPos.LMARGIN, new_y=YPos.NEXT, link=p["url"])
    pdf.set_text_color(50, 50, 50)
    pdf.ln(2)

# ── EXPERIENCE ────────────────────────────────────────────────
pdf.section_title("Professional Experience")
pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(20, 20, 20)
pdf.set_x(LM)
pdf.cell(TW, 5, "General Manager  |  Private Business, Buenos Aires  |  2016 - Present",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.bullet("Led and managed a team of up to 10 people in daily operations.")
pdf.bullet("Optimized operational processes and resolved high-pressure situations.")
pdf.bullet("Developed strong skills in communication, conflict resolution, and team coordination.")

# ── EDUCATION ─────────────────────────────────────────────────
pdf.section_title("Education & Certifications")

edu = [
    ("Universidad Nacional de Entre Rios (UNER)",
     "B.Tech in Web Development  |  2024 - Present"),
    ("ETH KIPU Latam",
     "Ethereum Developer Pack  |  2024  -  on-chain certificate"),
    ("Talento Tech - Buenos Aires Ministry of Education",
     "Node.js & React.js  |  2025  -  certified"),
    ("Codo a Codo - Buenos Aires Ministry of Education",
     "Full Stack Python + Django specialization  |  2022-2023  -  certified"),
    ("ISFA Manuel Belgrano",
     "National Teaching Degree in Visual Arts  |  2018-2024"),
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
         "Spanish - Native     |     English - Intermediate (actively improving, private lessons 2025)",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("/home/xtsulyts/Escritorio/portafolio/Walter_Frias_CV_2026.pdf")
print("CV generado: /home/xtsulyts/Escritorio/portafolio/Walter_Frias_CV_2026.pdf")
