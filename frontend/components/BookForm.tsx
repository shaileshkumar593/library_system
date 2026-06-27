"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import {
  useCreateBook,
  useUpdateBook,
} from "@/hooks/useBooks";

import {
  Book,
  CreateBookRequest,
} from "@/types/book";

interface Props {
  book?: Book;
}

export default function BookForm({
  book,
}: Props) {
  const router = useRouter();

  const createMutation = useCreateBook();

  const updateMutation = useUpdateBook();

  const [form, setForm] = useState<CreateBookRequest>({
    title: book?.title || "",

    author: book?.author || "",

    isbn: book?.isbn || "",

    publisher: book?.publisher || "",

    published_year: book?.published_year || 2025,

    total_copies: book?.total_copies || 1,
  });

  function handleChange(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    setForm({
      ...form,

      [e.target.name]:
        e.target.type === "number"
          ? Number(e.target.value)
          : e.target.value,
    });
  }

  async function handleSubmit(
    e: React.FormEvent
  ) {
    e.preventDefault();

    if (book) {
      await updateMutation.mutateAsync({
        id: book.id,
        data: form,
      });
    } else {
      await createMutation.mutateAsync(form);
    }

    router.push("/books");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
      />

      <br />

      <input
        name="author"
        placeholder="Author"
        value={form.author}
        onChange={handleChange}
      />

      <br />

      <input
        name="isbn"
        placeholder="ISBN"
        value={form.isbn}
        onChange={handleChange}
      />

      <br />

      <input
        name="publisher"
        placeholder="Publisher"
        value={form.publisher}
        onChange={handleChange}
      />

      <br />

      <input
        type="number"
        name="published_year"
        value={form.published_year}
        onChange={handleChange}
      />

      <br />

      <input
        type="number"
        name="total_copies"
        value={form.total_copies}
        onChange={handleChange}
      />

      <br />

      <button type="submit">
        {book ? "Update" : "Create"}
      </button>
    </form>
  );
}