def test_complete_borrow_flow(
    client,
):
    """
    Create Member

    Create Book

    Borrow Book

    Verify Inventory
    """

    ####################################################################
    # Create Member
    ####################################################################

    member = client.post(
        "/members",
        json={
            "full_name": "John",
            "email": "john@test.com",
            "phone": "9999999999",
            "address": "USA",
        },
    )

    assert member.status_code == 201

    member_id = member.json()["id"]

    ####################################################################
    # Create Book
    ####################################################################

    book = client.post(
        "/books",
        json={
            "title": "Clean Code",
            "author": "Robert Martin",
            "isbn": "1111",
            "publisher": "Pearson",
            "published_year": 2008,
            "total_copies": 5,
        },
    )

    assert book.status_code == 201

    book_json = book.json()

    book_id = book_json["id"]

    assert book_json["available_copies"] == 5

    ####################################################################
    # Borrow
    ####################################################################

    borrow = client.post(
        "/borrowings",
        json={
            "member_id": member_id,
            "book_id": book_id,
        },
    )

    assert borrow.status_code == 200

    body = borrow.json()

    assert body["status"] == "BORROWED"

    ####################################################################
    # Verify Inventory
    ####################################################################

    updated_book = client.get(
        f"/books/{book_id}"
    )

    assert updated_book.status_code == 200

    assert updated_book.json()["available_copies"] == 4

    ####################################################################
    # Borrow History
    ####################################################################

    history = client.get(
        f"/borrowings/member/{member_id}"
    )

    assert history.status_code == 200

    assert len(history.json()) == 1 