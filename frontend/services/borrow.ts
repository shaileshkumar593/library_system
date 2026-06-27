import api from "./api";
import {
    BorrowRequest,
    ReturnBookRequest,
    Borrowing,
} from "@/types/borrowing";

export async function borrowBook(
    payload: BorrowRequest
): Promise<Borrowing> {

    const { data } = await api.post(
        "/borrowings",
        payload
    );

    return data;
}

export async function returnBook(
    payload: ReturnBookRequest
): Promise<Borrowing> {

    const { data } = await api.post(
        "/borrowings/return",
        payload
    );

    return data;
}

export async function borrowedBooks(
    memberId: number
): Promise<Borrowing[]> {

    const { data } = await api.get(
        `/borrowings/member/${memberId}`
    );

    return data;
}