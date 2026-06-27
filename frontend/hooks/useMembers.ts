"use client";

import {
    useMutation,
    useQuery,
    useQueryClient,
} from "@tanstack/react-query";

import {
    getMembers,
    getMember,
    createMember,
    updateMember,
    deleteMember,
} from "@/services/members";

export function useMembers() {
    return useQuery({
        queryKey: ["members"],
        queryFn: getMembers,
    });
}

export function useMember(id: number) {
    return useQuery({
        queryKey: ["member", id],
        queryFn: () => getMember(id),
        enabled: !!id,
    });
}

export function useCreateMember() {
    const qc = useQueryClient();

    return useMutation({
        mutationFn: createMember,
        onSuccess() {
            qc.invalidateQueries({
                queryKey: ["members"],
            });
        },
    });
}

export function useUpdateMember() {
    const qc = useQueryClient();

    return useMutation({
        mutationFn: ({
            id,
            data,
        }: {
            id: number;
            data: any;
        }) => updateMember(id, data),

        onSuccess() {
            qc.invalidateQueries({
                queryKey: ["members"],
            });
        },
    });
}

export function useDeleteMember() {
    const qc = useQueryClient();

    return useMutation({
        mutationFn: deleteMember,

        onSuccess() {
            qc.invalidateQueries({
                queryKey: ["members"],
            });
        },
    });
}