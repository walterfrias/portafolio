import swapImg from '../assets/swap.png';
import daoImg from '../assets/dao.png';
import cooperadoraImg from '../assets/cooperadora.png';
import gestorImg from '../assets/gestor.png';
import comandaImg from '../assets/comanda.png';
import botsImg from '../assets/bots.jpg';

// `secondary` projects are listed under "Other work", after the main ones.
export const projects = [
  {
    name: "Comanda — Restaurant Management SaaS",
    description:
      "Multi-tenant SaaS for restaurant operations, used daily by 10 users across 2 restaurants and saving an estimated 40+ hours of manual work per month. Recipe costs and margins update automatically when supplier prices change, across 8 unit types. Includes stock counts, supplier orders via WhatsApp, daily cash and monthly cost reports, and 7 role-based views. In development: a mobile app where managers photograph a supplier invoice and Claude's vision model extracts supplier, date, line items and total as structured data, flagging anything unreadable. The manager reviews and confirms before anything is saved.",
    tags: ["Django REST", "Python", "PostgreSQL", "React", "TypeScript", "PWA", "React Native", "Expo", "Claude API", "Structured outputs"],
    url: "https://www.comanda.com.ar/",
    devpost: null,
    badge: "In production",
    image: comandaImg,
    objectPosition: "object-left-top",
    // Long description: taller card so the screenshot still shows above the text.
    cardHeight: "min-h-96 md:min-h-[38rem] xl:min-h-[34rem]",
  },
  {
    name: "Automated Trading Bots — Hyperliquid",
    description:
      "Two bots I built and operate, trading real capital 24/7 on my own Ubuntu server. HL-Delta runs a delta-neutral funding-rate strategy; HL-Spot trades BTC on a backtested signal with partial take-profits. Both report status to Telegram. After a silent order failure caused a loss in production, I wrote the postmortem and shipped the fixes.",
    tags: ["Python", "asyncio", "Hyperliquid SDK", "systemd", "Ubuntu Server", "Telegram Bot API", "Backtesting"],
    url: null,
    devpost: null,
    badge: "Live 24/7",
    image: botsImg,
    objectPosition: "object-center",
    cardHeight: "min-h-96 md:min-h-[34rem] xl:min-h-[30rem]",
  },
  {
    name: "CooperaApp — Transparency for School Cooperatives",
    description:
      "As president of a school cooperative, I saw parents distrust it: dues and funds lived only inside the cooperative, with no way to share them. CooperaApp shows every family paid dues, funds raised and school news. It rolls out in 2027 without blockchain — parents don't need a DAO to trust the numbers. A DAO-per-school version (testnet) is built for scaling later.",
    tags: ["Django REST", "React", "TypeScript", "Vite", "PostgreSQL", "Docker", "Solidity"],
    url: "https://cooperadora-escuela-27.vercel.app/",
    devpost: null,
    badge: ["Web2 + Web3", "Launching 2027"],
    image: cooperadoraImg,
    objectPosition: "object-top",
    cardHeight: "min-h-96 md:min-h-[34rem] xl:min-h-[30rem]",
  },
  {
    name: "DAO — Hackathon Ethereum 2024",
    description:
      "DAO built in 48 hours at the ETH KIPU Latam Academic Hackathon. Awarded first place among all participating teams.",
    tags: ["Solidity", "Hardhat", "Scaffold-ETH", "Next.js", "React", "TypeScript", "TailwindCSS"],
    url: "https://hackatonbuildingdao.vercel.app/",
    devpost: "https://devpost.com/software/buildingdao-democratic-desicion-making#",
    badge: "🥇 1st place",
    image: daoImg,
    contain: true,
    secondary: true,
  },
  {
    name: "ERC-20 Token Pool / Swap",
    description:
      "ERC-20 token swap system with added liquidity. Smart contracts connected to a live React interface deployed in production.",
    tags: ["Solidity", "TypeScript", "React", "Vite", "Hardhat", "TailwindCSS"],
    url: "https://swaperc20.netlify.app/",
    devpost: null,
    badge: null,
    image: swapImg,
    secondary: true,
  },
  {
    name: "Project Management System",
    description:
      "Project management platform with role-based access, Kanban workflow and CSV export. Angular + NestJS + PostgreSQL, dockerized.",
    tags: ["Angular", "NestJS", "TypeScript", "PostgreSQL", "Docker"],
    url: "https://integrador-des-app-web.vercel.app/",
    devpost: null,
    badge: null,
    image: gestorImg,
    objectPosition: "object-top",
    secondary: true,
  },
];
