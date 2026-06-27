"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const menus = [
  { title: "Dashboard", href: "/" },
  { title: "Books", href: "/books" },
  { title: "Members", href: "/members" },
  { title: "Borrow", href: "/borrow" },
  { title: "History", href: "/history" },
];

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "18px 40px",
        background: "#2563eb",
        color: "white",
      }}
    >
      <h2>📚 Library Management</h2>

      <div style={{ display: "flex", gap: 25 }}>
        {menus.map((menu) => (
          <Link
            key={menu.href}
            href={menu.href}
            style={{
              color: pathname === menu.href ? "#FACC15" : "white",
              textDecoration: "none",
              fontWeight: 600,
            }}
          >
            {menu.title}
          </Link>
        ))}
      </div>
    </nav>
  );
}