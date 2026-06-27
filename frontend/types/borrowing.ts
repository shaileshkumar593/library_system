// frontend/types/borrowing.ts

/**
 * Borrowing status returned by the backend.
 */
export type BorrowStatus =
  | "BORROWED"
  | "RETURNED"
  | "OVERDUE";

/**
 * Borrowing record.
 */
export interface Borrowing {
  id: number;
  member_id: number;
  book_id: number;

  borrow_date: string;

  due_date: string;

  return_date?: string;

  status: BorrowStatus;
}

/**
 * Borrow request payload.
 */
export interface BorrowBookRequest {
  member_id: number;
  book_id: number;
}

/**
 * Return book request payload.
 */
export interface ReturnBookRequest {
  borrowing_id: number;
}

/**
 * Response from borrow/return API.
 */
export type BorrowResponse = Borrowing;