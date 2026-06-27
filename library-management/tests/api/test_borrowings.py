###########################################################################
# BORROW BOOK
###########################################################################

def test_borrow_book(

    client,

    sample_member,

    sample_book,
):

    response = client.post(

        "/borrowings",

        json={

            "member_id": sample_member.id,

            "book_id": sample_book.id,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "BORROWED"


###########################################################################
# INVALID MEMBER
###########################################################################

def test_invalid_member(client):

    response = client.post(

        "/borrowings",

        json={

            "member_id": 999,

            "book_id": 1,
        },
    )

    assert response.status_code == 404


###########################################################################
# INVALID BOOK
###########################################################################

def test_invalid_book(
    client,
    sample_member,
):

    response = client.post(

        "/borrowings",

        json={

            "member_id": sample_member.id,

            "book_id": 999,
        },
    )

    assert response.status_code == 404


###########################################################################
# RETURN BOOK
###########################################################################

def test_return_book(
    client,
    sample_borrowing,
):

    response = client.post(

        "/borrowings/return",

        json={

            "borrowing_id": sample_borrowing.id
        },
    )

    assert response.status_code == 200

    assert response.json()["status"] == "RETURNED"


###########################################################################
# RETURN TWICE
###########################################################################

def test_return_twice(
    client,
    sample_borrowing,
):

    client.post(

        "/borrowings/return",

        json={

            "borrowing_id": sample_borrowing.id
        },
    )

    response = client.post(

        "/borrowings/return",

        json={

            "borrowing_id": sample_borrowing.id
        },
    )

    assert response.status_code == 400


###########################################################################
# BORROW HISTORY
###########################################################################

def test_member_borrow_history(
    client,
    sample_borrowing,
):

    response = client.get(

        f"/borrowings/member/{sample_borrowing.member_id}"
    )

    assert response.status_code == 200

    assert len(response.json()) == 1