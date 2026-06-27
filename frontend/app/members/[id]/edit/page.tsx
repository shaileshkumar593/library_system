"use client";

import { useParams } from "next/navigation";

import Layout from "@/components/Layout";

import Loader from "@/components/Loader";

import MemberForm from "@/components/MemberForm";

import { useMember } from "@/hooks/useMembers";

export default function(){

const params=useParams();

const id=Number(params.id);

const{

data,

isLoading,

}=useMember(id);

if(isLoading){

return <Loader/>

}

if(!data){

return <h1>Not Found</h1>

}

return(

<Layout>

<h1>Edit Member</h1>

<MemberForm member={data}/>

</Layout>

)

}