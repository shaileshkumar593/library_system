"use client";

import Link from "next/link";
import { Book } from "@/types/book";
import { useDeleteBook } from "@/hooks/useBooks";

interface Props {
  books: Book[];
}

export default function BookTable({ books }: Props) {
  const deleteMutation = useDeleteBook();

  function handleDelete(id: number) {
    if (!confirm("Delete this book?")) return;

    deleteMutation.mutate(id);
  }

  return (
    <table
      style={{
        width: "100%",
        borderCollapse: "collapse",
      }}
    >
      <thead>
        <tr>
          <th>ID</th>

          <th>Title</th>

          <th>Author</th>

          <th>Available</th>

          <th>Action</th>
        </tr>
      </thead>

      <tbody>
        {books.map((book) => (
          <tr key={book.id}>
            <td>{book.id}</td>

            <td>{book.title}</td>

            <td>{book.author}</td>

            <td>{book.available_copies}</td>

            <td>
              <Link href={`/books/${book.id}/edit`}>
                Edit
              </Link>

              {" | "}

              <button
                onClick={() => handleDelete(book.id)}
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}