###########################################################################
# CREATE MEMBER
###########################################################################

def test_create_member(client):

    payload = {

        "full_name": "John",

        "email": "john@test.com",

        "phone": "999999999",

        "address": "USA",
    }

    response = client.post(
        "/members",
        json=payload,
    )

    assert response.status_code == 201

    body = response.json()

    assert body["email"] == "john@test.com"


###########################################################################
# DUPLICATE EMAIL
###########################################################################

def test_duplicate_email(
    client,
    sample_member,
):

    payload = {

        "full_name": "John",

        "email": sample_member.email,

        "phone": "999999999",

        "address": "USA",
    }

    response = client.post(
        "/members",
        json=payload,
    )

    assert response.status_code == 409


###########################################################################
# GET MEMBER
###########################################################################

def test_get_member(
    client,
    sample_member,
):

    response = client.get(
        f"/members/{sample_member.id}"
    )

    assert response.status_code == 200


###########################################################################
# LIST MEMBERS
###########################################################################

def test_list_members(
    client,
    multiple_members,
):

    response = client.get("/members")

    assert response.status_code == 200

    assert len(response.json()) == 5


###########################################################################
# UPDATE MEMBER
###########################################################################

def test_update_member(
    client,
    sample_member,
):

    response = client.put(

        f"/members/{sample_member.id}",

        json={
            "full_name": "Jane"
        },
    )

    assert response.status_code == 200

    assert response.json()["full_name"] == "Jane"


###########################################################################
# DELETE MEMBER
###########################################################################

def test_delete_member(
    client,
    sample_member,
):

    response = client.delete(
        f"/members/{sample_member.id}"
    )

    assert response.status_code == 204