"use client";

import { useParams } from "next/navigation";

import Layout from "@/components/Layout";

import Loader from "@/components/Loader";

import BookForm from "@/components/BookForm";

import { useBook } from "@/hooks/useBooks";

export default function EditBook() {
  const params = useParams();

  const id = Number(params.id);

  const {
    data,
    isLoading,
  } = useBook(id);

  if (isLoading)
    return <Loader />;

  if (!data)
    return <h2>Book not found.</h2>;

  return (
    <Layout>
      <h1>Edit Book</h1>

      <BookForm
        book={data}
      />
    </Layout>
  );
}