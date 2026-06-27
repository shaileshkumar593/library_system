import api from "./api";
import {
    Member,
    CreateMemberRequest,
    UpdateMemberRequest,
} from "@/types/member";

export async function getMembers(): Promise<Member[]> {
    const { data } = await api.get("/members");
    return data;
}

export async function getMember(
    id: number
): Promise<Member> {
    const { data } = await api.get(`/members/${id}`);
    return data;
}

export async function createMember(
    payload: CreateMemberRequest
) {
    const { data } = await api.post(
        "/members",
        payload
    );

    return data;
}

export async function updateMember(
    id: number,
    payload: UpdateMemberRequest
) {
    const { data } = await api.put(
        `/members/${id}`,
        payload
    );

    return data;
}

export async function deleteMember(
    id: number
) {
    await api.delete(`/members/${id}`);
}