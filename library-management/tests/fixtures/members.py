import pytest

from app.models.member import Member


@pytest.fixture
def sample_member(db):

    member = Member(

        full_name="John Doe",

        email="john@example.com",

        phone="9999999999",

        address="New York",
    )

    db.add(member)

    db.commit()

    db.refresh(member)

    return member


@pytest.fixture
def multiple_members(db):

    members = []

    for i in range(5):

        member = Member(

            full_name=f"Member {i}",

            email=f"user{i}@mail.com",

            phone="9999999999",

            address="City",
        )

        db.add(member)

        members.append(member)

    db.commit()

    return members