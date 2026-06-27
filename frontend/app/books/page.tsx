"use client";

import Link from "next/link";

import Layout from "@/components/Layout";

import Loader from "@/components/Loader";

import BookTable from "@/components/BookTable";

import { useBooks } from "@/hooks/useBooks";

export default function BooksPage() {
  const {
    data,
    isLoading,
    error,
  } = useBooks();

  if (isLoading)
    return <Loader />;

  if (error)
    return <h2>Error loading books.</h2>;

  return (
    <Layout>
      <h1>Books</h1>

      <br />

      <Link href="/books/new">
        Add Book
      </Link>

      <br />

      <br />

      <BookTable
        books={data ?? []}
      />
    </Layout>
  );
}