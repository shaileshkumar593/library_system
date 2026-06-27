// frontend/types/book.ts

/**
 * Represents a book returned by the backend.
 */
export interface Book {
  id: number;
  title: string;
  author: string;
  isbn: string;
  publisher?: string;
  published_year?: number;
  total_copies: number;
  available_copies: number;
}

/**
 * Payload used to create a new book.
 */
export interface CreateBookRequest {
  title: string;
  author: string;
  isbn: string;
  publisher?: string;
  published_year?: number;
  total_copies: number;
}

/**
 * Payload used to update an existing book.
 */
export interface UpdateBookRequest {
  title?: string;
  author?: string;
  isbn?: string;
  publisher?: string;
  published_year?: number;
  total_copies?: number;
}

/**
 * Response received after creating/updating a book.
 */
export type BookResponse = Book;