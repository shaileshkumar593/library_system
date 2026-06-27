// frontend/types/member.ts

/**
 * Represents a library member.
 */
export interface Member {
  id: number;
  full_name: string;
  email: string;
  phone: string;
  address?: string;
}

/**
 * Payload used to create a member.
 */
export interface CreateMemberRequest {
  full_name: string;
  email: string;
  phone: string;
  address?: string;
}

/**
 * Payload used to update a member.
 */
export interface UpdateMemberRequest {
  full_name?: string;
  email?: string;
  phone?: string;
  address?: string;
}

/**
 * Response returned by the backend.
 */
export type MemberResponse = Member;