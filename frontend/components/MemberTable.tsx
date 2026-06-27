"use client";

import Link from "next/link";

import { Member } from "@/types/member";

import { useDeleteMember } from "@/hooks/useMembers";

interface Props {
    members: Member[];
}

export default function MemberTable({
    members,
}: Props) {

    const deleteMutation =
        useDeleteMember();

    return (

<table border={1}
cellPadding={10}
width="100%">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Email</th>

<th>Phone</th>

<th>Action</th>

</tr>

</thead>

<tbody>

{members.map(member=>(

<tr key={member.id}>

<td>{member.id}</td>

<td>{member.full_name}</td>

<td>{member.email}</td>

<td>{member.phone}</td>

<td>

<Link
href={`/members/${member.id}/edit`}>

Edit

</Link>

{" | "}

<button

onClick={()=>{

if(confirm("Delete?")){

deleteMutation.mutate(member.id)

}

}}

>

Delete

</button>

</td>

</tr>

))}

</tbody>

</table>

)

}