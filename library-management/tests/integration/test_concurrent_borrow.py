from concurrent.futures import ThreadPoolExecutor


def borrow(client, member_id, book_id):

    return client.post(
        "/borrowings",
        json={
            "member_id": member_id,
            "book_id": book_id,
        },
    )


def test_only_one_user_gets_last_book(client):

    ####################################################################
    # Book
    ####################################################################

    book = client.post(
        "/books",
        json={
            "title": "Distributed Systems",
            "author": "Martin",
            "isbn": "3333",
            "publisher": "ABC",
            "published_year": 2024,
            "total_copies": 1,
        },
    )

    book_id = book.json()["id"]

    ####################################################################
    # Member 1
    ####################################################################

    member1 = client.post(
        "/members",
        json={
            "full_name": "User1",
            "email": "user1@test.com",
            "phone": "999",
            "address": "USA",
        },
    )

    member2 = client.post(
        "/members",
        json={
            "full_name": "User2",
            "email": "user2@test.com",
            "phone": "999",
            "address": "USA",
        },
    )

    member1_id = member1.json()["id"]

    member2_id = member2.json()["id"]

    ####################################################################
    # Concurrent Borrow
    ####################################################################

    with ThreadPoolExecutor(max_workers=2) as executor:

        future1 = executor.submit(
            borrow,
            client,
            member1_id,
            book_id,
        )

        future2 = executor.submit(
            borrow,
            client,
            member2_id,
            book_id,
        )

    response1 = future1.result()

    response2 = future2.result()

    success = [
        r for r in [response1, response2]
        if r.status_code == 200
    ]

    failed = [
        r for r in [response1, response2]
        if r.status_code == 400
    ]

    assert len(success) == 1

    assert len(failed) == 1

    ####################################################################
    # Inventory
    ####################################################################

    updated = client.get(
        f"/books/{book_id}"
    )

    assert updated.json()["available_copies"] == 0