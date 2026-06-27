"use client";

import { useState } from "react";

import { useRouter } from "next/navigation";

import {
    useCreateMember,
    useUpdateMember,
} from "@/hooks/useMembers";

import {
    Member,
    CreateMemberRequest,
} from "@/types/member";

interface Props {
    member?: Member;
}

export default function MemberForm({
    member,
}: Props) {

const router=useRouter();

const createMutation=
useCreateMember();

const updateMutation=
useUpdateMember();

const [form,setForm]=
useState<CreateMemberRequest>({

full_name:
member?.full_name||"",

email:
member?.email||"",

phone:
member?.phone||"",

address:
member?.address||"",

});

function handleChange(
e:React.ChangeEvent<HTMLInputElement>
){

setForm({

...form,

[e.target.name]:
e.target.value,

});

}

async function submit(
e:React.FormEvent
){

e.preventDefault();

if(member){

await updateMutation.mutateAsync({

id:member.id,

data:form,

});

}else{

await createMutation.mutateAsync(form);

}

router.push("/members");

}

return(

<form onSubmit={submit}>

<input

name="full_name"

placeholder="Name"

value={form.full_name}

onChange={handleChange}

/>

<br/>

<input

name="email"

placeholder="Email"

value={form.email}

onChange={handleChange}

/>

<br/>

<input

name="phone"

placeholder="Phone"

value={form.phone}

onChange={handleChange}

/>

<br/>

<input

name="address"

placeholder="Address"

value={form.address}

onChange={handleChange}

/>

<br/>

<button>

{member?"Update":"Create"}

</button>

</form>

)

}