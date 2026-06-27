from datetime import datetime

from app.models.borrowing import BorrowStatus
from app.repository.borrowing_repository import BorrowRepository


repo = BorrowRepository()


def test_create_borrowing(
    db,
    sample_book,
    sample_member,
):

    borrowing = repo.create(

        db=db,

        member_id=sample_member.id,

        book_id=sample_book.id,

        due_date=datetime.utcnow(),
    )

    db.commit()

    assert borrowing.id is not None
    assert borrowing.status == BorrowStatus.BORROWED


def test_get_borrowing(
    db,
    sample_borrowing,
):

    borrowing = repo.get(
        db,
        sample_borrowing.id,
    )

    assert borrowing.id == sample_borrowing.id


def test_list_borrowings(
    db,
    sample_borrowing,
):

    borrowings = repo.list(db)

    assert len(borrowings) == 1


def test_get_active_member_books(
    db,
    sample_borrowing,
):

    records = repo.get_active_by_member(
        db,
        sample_borrowing.member_id,
    )

    assert len(records) == 1


def test_update_status(
    db,
    sample_borrowing,
):

    borrowing = repo.update_status(

        db,

        sample_borrowing,

        BorrowStatus.RETURNED,

        datetime.utcnow(),
    )

    db.commit()

    assert borrowing.status == BorrowStatus.RETURNED
    assert borrowing.return_date is not None


def test_delete_borrowing(
    db,
    sample_borrowing,
):

    repo.delete(
        db,
        sample_borrowing,
    )

    db.commit()

    borrowing = repo.get(
        db,
        sample_borrowing.id,
    )

    assert borrowing is None