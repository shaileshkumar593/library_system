from app.models.book import Book


###########################################################################
# CREATE BOOK
###########################################################################

def test_create_book(client):

    payload = {
        "title": "Clean Code",
        "author": "Robert Martin",
        "isbn": "9780132350884",
        "publisher": "Pearson",
        "published_year": 2008,
        "total_copies": 5
    }

    response = client.post(
        "/books",
        json=payload,
    )

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == "Clean Code"

    assert body["available_copies"] == 5


###########################################################################
# INVALID BODY
###########################################################################

def test_create_book_invalid(client):

    response = client.post(
        "/books",
        json={}
    )

    assert response.status_code == 422


###########################################################################
# GET BOOK
###########################################################################

def test_get_book(
    client,
    sample_book,
):

    response = client.get(
        f"/books/{sample_book.id}"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == sample_book.id


###########################################################################
# BOOK NOT FOUND
###########################################################################

def test_book_not_found(client):

    response = client.get("/books/999")

    assert response.status_code == 404


###########################################################################
# LIST BOOKS
###########################################################################

def test_list_books(
    client,
    multiple_books,
):

    response = client.get("/books")

    assert response.status_code == 200

    books = response.json()

    assert len(books) == 5


###########################################################################
# UPDATE BOOK
###########################################################################

def test_update_book(
    client,
    sample_book,
):

    payload = {
        "title": "Advanced Python"
    }

    response = client.put(
        f"/books/{sample_book.id}",
        json=payload,
    )

    assert response.status_code == 200

    assert response.json()["title"] == "Advanced Python"


###########################################################################
# DELETE BOOK
###########################################################################

def test_delete_book(
    client,
    sample_book,
):

    response = client.delete(
        f"/books/{sample_book.id}"
    )

    assert response.status_code == 204