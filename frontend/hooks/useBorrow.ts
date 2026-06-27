"use client";

import {
    useMutation,
    useQuery,
    useQueryClient,
} from "@tanstack/react-query";

import {
    borrowBook,
    borrowedBooks,
    returnBook,
} from "@/services/borrow";

export function useBorrowedBooks(
    memberId: number
) {

    return useQuery({

        queryKey: ["borrowings", memberId],

        queryFn: () => borrowedBooks(memberId),

        enabled: memberId > 0,

    });

}

export function useBorrowBook() {

    const qc = useQueryClient();

    return useMutation({

        mutationFn: borrowBook,

        onSuccess() {

            qc.invalidateQueries({
                queryKey: ["books"],
            });

            qc.invalidateQueries({
                queryKey: ["borrowings"],
            });

        },

    });

}

export function useReturnBook() {

    const qc = useQueryClient();

    return useMutation({

        mutationFn: returnBook,

        onSuccess() {

            qc.invalidateQueries({
                queryKey: ["books"],
            });

            qc.invalidateQueries({
                queryKey: ["borrowings"],
            });

        },

    });

}