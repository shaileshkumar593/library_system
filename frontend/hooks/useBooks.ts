"use client";

import {

useQuery,

useMutation,

useQueryClient,

} from "@tanstack/react-query";

import {

createBook,

deleteBook,

updateBook,

} from "../services/books";


import { getBook } from "@/services/books";

export function useBook(id: number) {
  return useQuery({
    queryKey: ["book", id],
    queryFn: () => getBook(id),
    enabled: !!id,
  });
}

export function useCreateBook(){

const queryClient=useQueryClient();

return useMutation({

mutationFn:createBook,

onSuccess:()=>{

queryClient.invalidateQueries({

queryKey:["books"],

});

},

});

}

export function useDeleteBook(){

const queryClient=useQueryClient();

return useMutation({

mutationFn:deleteBook,

onSuccess:()=>{

queryClient.invalidateQueries({

queryKey:["books"],

});

},

});

}

export function useUpdateBook(){

const queryClient=useQueryClient();

return useMutation({

mutationFn:({

id,

data,

}:{

id:number;

data:any;

})=>updateBook(id,data),

onSuccess:()=>{

queryClient.invalidateQueries({

queryKey:["books"],

});

},

});

}