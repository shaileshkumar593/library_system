"use client";

import Link from "next/link";

import Layout from "@/components/Layout";

import Loader from "@/components/Loader";

import MemberTable from "@/components/MemberTable";

import { useMembers } from "@/hooks/useMembers";

export default function MembersPage(){

const{

data,

isLoading,

}=useMembers();

if(isLoading){

return <Loader/>

}

return(

<Layout>

<h1>Members</h1>

<br/>

<Link href="/members/new">

Add Member

</Link>

<br/>

<br/>

<MemberTable

members={data??[]}

/>

</Layout>

)

}