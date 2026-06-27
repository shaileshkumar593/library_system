"use client";

import Link from "next/link";

export default function Sidebar() {
  return (
    <aside
      style={{
        width: 220,
        background: "#1e293b",
        color: "white",
        minHeight: "100vh",
        padding: 20,
      }}
    >
      <h2>Library</h2>

      <hr />

      <ul
        style={{
          listStyle: "none",
          padding: 0,
        }}
      >
        <li>
          <Link href="/">Dashboard</Link>
        </li>

        <li>
          <Link href="/books">Books</Link>
        </li>

        <li>
          <Link href="/members">Members</Link>
        </li>

        <li>
          <Link href="/borrow">Borrow</Link>
        </li>

        <li>
          <Link href="/history">History</Link>
        </li>
      </ul>
    </aside>
  );
}