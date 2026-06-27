from app.repository.member_repository import MemberRepository
from app.schemas.member import MemberCreate
from app.schemas.member import MemberUpdate


repo = MemberRepository()


def test_create_member(db):

    payload = MemberCreate(

        full_name="Alice",

        email="alice@test.com",

        phone="999999999",

        address="USA",
    )

    member = repo.create(
        db,
        payload,
    )

    db.commit()

    assert member.id is not None
    assert member.email == "alice@test.com"


def test_get_member(db, sample_member):

    member = repo.get(
        db,
        sample_member.id,
    )

    assert member.full_name == "John Doe"


def test_get_invalid_member(db):

    member = repo.get(
        db,
        100,
    )

    assert member is None


def test_get_by_email(db, sample_member):

    member = repo.get_by_email(
        db,
        sample_member.email,
    )

    assert member.email == sample_member.email


def test_list_members(db, multiple_members):

    members = repo.list(db)

    assert len(members) == 5


def test_update_member(db, sample_member):

    payload = MemberUpdate(

        full_name="Jane Doe",
    )

    updated = repo.update(
        db,
        sample_member,
        payload,
    )

    db.commit()

    assert updated.full_name == "Jane Doe"


def test_delete_member(db, sample_member):

    repo.delete(
        db,
        sample_member,
    )

    db.commit()

    member = repo.get(
        db,
        sample_member.id,
    )

    assert member is None