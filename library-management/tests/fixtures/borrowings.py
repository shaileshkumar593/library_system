from datetime import datetime
from datetime import timedelta

import pytest

from app.models.borrowing import Borrowing
from app.models.borrowing import BorrowStatus


@pytest.fixture
def sample_borrowing(
    db,
    sample_member,
    sample_book,
):

    borrowing = Borrowing(

        member_id=sample_member.id,

        book_id=sample_book.id,

        borrow_date=datetime.utcnow(),

        due_date=datetime.utcnow() + timedelta(days=14),

        status=BorrowStatus.BORROWED,
    )

    sample_book.available_copies -= 1

    db.add(borrowing)

    db.commit()

    db.refresh(borrowing)

    return borrowing