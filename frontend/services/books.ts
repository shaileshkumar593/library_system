import api from "./api";
import { Book } from "../types/book";

export async function getBooks(): Promise<Book[]> {
    const response = await api.get("/books");
    return response.data;
}


export async function getBook(
  id: number
): Promise<Book> {
  const response = await api.get(
    `/books/${id}`
  );

  return response.data;
}

export async function createBook(
    data: Omit<Book, "id" | "available_copies">
) {
    const response = await api.post(
        "/books",
        data
    );

    return response.data;
}

export async function updateBook(
    id: number,
    data: Partial<Book>
) {
    const response = await api.put(
        `/books/${id}`,
        data
    );

    return response.data;
}

export async function deleteBook(id: number) {
    return api.delete(`/books/${id}`);
}

