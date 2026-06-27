def test_complete_return_flow(
    client,
):
    """
    Borrow

    Return

    Inventory Restored

    Status Updated
    """

    ####################################################################
    # Create Member
    ####################################################################

    member = client.post(
        "/members",
        json={
            "full_name": "Alice",
            "email": "alice@test.com",
            "phone": "999999999",
            "address": "India",
        },
    )

    member_id = member.json()["id"]

    ####################################################################
    # Create Book
    ####################################################################

    book = client.post(
        "/books",
        json={
            "title": "Python",
            "author": "Guido",
            "isbn": "2222",
            "publisher": "ABC",
            "published_year": 2024,
            "total_copies": 3,
        },
    )

    book_id = book.json()["id"]

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

    borrowing_id = borrow.json()["id"]

    ####################################################################
    # Return
    ####################################################################

    returned = client.post(
        "/borrowings/return",
        json={
            "borrowing_id": borrowing_id
        },
    )

    assert returned.status_code == 200

    assert returned.json()["status"] == "RETURNED"

    ####################################################################
    # Verify Inventory
    ####################################################################

    updated = client.get(
        f"/books/{book_id}"
    )

    assert updated.json()["available_copies"] == 3

    ####################################################################
    # Verify History
    ####################################################################

    history = client.get(
        f"/borrowings/member/{member_id}"
    )

    # Only active borrowings are returned by the endpoint
    assert history.status_code == 200
    assert len(history.json()) == 0