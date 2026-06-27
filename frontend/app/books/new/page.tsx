import Layout from "@/components/Layout";

import BookForm from "@/components/BookForm";

export default function NewBook() {
  return (
    <Layout>
      <h1>Add Book</h1>

      <BookForm />
    </Layout>
  );
}