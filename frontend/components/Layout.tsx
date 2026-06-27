"use client";

export default function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <main
      style={{
        maxWidth: 1200,
        margin: "30px auto",
        padding: 20,
      }}
    >
      {children}
    </main>
  );
}