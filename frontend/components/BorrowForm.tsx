"use client";

import { useState } from "react";

import { useBooks } from "@/hooks/useBooks";

import { useMembers } from "@/hooks/useMembers";

import { useBorrowBook } from "@/hooks/useBorrow";

export default function BorrowForm() {

    const { data: books } = useBooks();

    const { data: members } = useMembers();

    const mutation = useBorrowBook();

    const [memberId, setMemberId] = useState(0);

    const [bookId, setBookId] = useState(0);

    async function submit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        if (!memberId || !bookId) {

            alert("Select member and book");

            return;
        }

        await mutation.mutateAsync({

            member_id: memberId,

            book_id: bookId,

        });

        alert("Book Borrowed");

        setBookId(0);

        setMemberId(0);

    }

    return (

<form onSubmit={submit}>

<h2>Borrow Book</h2>

<br/>

<label>

Member

</label>

<br/>

<select

value={memberId}

onChange={(e)=>

setMemberId(Number(e.target.value))

}

>

<option value={0}>

Select Member

</option>

{members?.map(member=>(

<option

key={member.id}

value={member.id}

>

{member.full_name}

</option>

))}

</select>

<br/>

<br/>

<label>

Book

</label>

<br/>

<select

value={bookId}

onChange={(e)=>

setBookId(Number(e.target.value))

}

>

<option value={0}>

Select Book

</option>

{books

?.filter(

book=>book.available_copies>0

)

.map(book=>(

<option

key={book.id}

value={book.id}

>

{book.title}

({book.available_copies})

</option>

))}

</select>

<br/>

<br/>

<button>

Borrow Book

</button>

</form>

)

}