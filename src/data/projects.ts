import swapImg from '../assets/swap.png';
import ecommerceImg from '../assets/ecommerce.png';
import daoImg from '../assets/dao.png';
import cooperadoraImg from '../assets/cooperadora.png';
import cooperadoraDaoImg from '../assets/cooperadora_dao.png';
import gestorImg from '../assets/gestor.png';
import comandaImg from '../assets/comanda.png';

export const projects = [
  {
    name: "Comanda — Restaurant Management SaaS",
    description:
      "Multi-tenant SaaS for restaurant operations, used daily in a real restaurant. Recipe costs and margins update automatically when supplier prices change, across 8 unit types. Includes stock counts, supplier orders via WhatsApp, daily cash and monthly cost reports, and 7 role-based views. Native mobile app in progress.",
    tags: ["Django REST", "PostgreSQL", "React", "TypeScript", "PWA", "React Native", "Expo"],
    url: "https://comanda-orcin.vercel.app/",
    devpost: null,
    badge: "In production",
    image: comandaImg,
    objectPosition: "object-left-top",
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
  },
  {
    name: "CooperaApp — SaaS for School Cooperatives",
    description:
      "Multi-tenant SaaS platform for Argentine school cooperatives. Each school gets its own DAO deployed on Base Sepolia via a Factory contract, with an ERC-20 COOP token minted per paid due. Includes 6-role RBAC, payment tracking, student enrollment and on-chain voting.",
    tags: ["Django REST", "React", "TypeScript", "Vite", "PostgreSQL", "Docker", "Solidity"],
    url: "https://cooperadora-escuela-27.vercel.app/",
    devpost: null,
    badge: "Web2 + Web3",
    image: cooperadoraImg,
    objectPosition: "object-top",
  },
  {
    name: "Project Management System",
    description:
      "Fullstack project management app with role-based access (Admin/Operator), Kanban board, advanced filtering, pagination and CSV export. Built as the final project for Software Engineering at UNER.",
    tags: ["Angular", "NestJS", "TypeScript", "PostgreSQL", "Docker"],
    url: "https://integrador-des-app-web.vercel.app/",
    devpost: null,
    badge: null,
    image: gestorImg,
    objectPosition: "object-top",
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
  },
  {
    name: "E-commerce B2C",
    description:
      "Online sales platform with a decoupled frontend and REST backend. Deployed in production with Firebase integration.",
    tags: ["React", "Vite", "JavaScript", "Node.js", "Express", "Firebase", "TailwindCSS"],
    url: "https://eshopdevices.netlify.app/",
    devpost: null,
    badge: null,
    image: ecommerceImg,
    objectPosition: "object-left md:object-top",
  },
];
