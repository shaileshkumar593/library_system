from datetime import datetime

from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from app.models.book import Book
from app.models.borrowing import BorrowStatus
from app.models.borrowing import Borrowing
from app.models.member import Member

from app.services.borrow_service import BorrowService


@pytest.fixture
def service():

    service = BorrowService()

    service.book_repo = MagicMock()
    service.member_repo = MagicMock()
    service.borrow_repo = MagicMock()

    return service


def test_borrow_success(service):

    member = Member(id=1)

    book = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        total_copies=5,
        available_copies=5,
    )

    borrowing = Borrowing(id=1)

    service.member_repo.get.return_value = member

    service.book_repo.get.return_value = book

    service.borrow_repo.create.return_value = borrowing

    db = MagicMock()

    result = service.borrow_book(
        db,
        1,
        1,
    )

    assert result.id == 1

    db.commit.assert_called_once()


def test_book_not_found(service):

    service.member_repo.get.return_value = Member(id=1)

    service.book_repo.get.return_value = None

    with pytest.raises(HTTPException):

        service.borrow_book(
            MagicMock(),
            1,
            1,
        )


def test_member_not_found(service):

    service.member_repo.get.return_value = None

    with pytest.raises(HTTPException):

        service.borrow_book(
            MagicMock(),
            1,
            1,
        )


def test_book_unavailable(service):

    service.member_repo.get.return_value = Member(id=1)

    service.book_repo.get.return_value = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        total_copies=5,
        available_copies=0,
    )

    with pytest.raises(HTTPException):

        service.borrow_book(
            MagicMock(),
            1,
            1,
        )


def test_return_book(service):

    borrowing = Borrowing(
        id=1,
        status=BorrowStatus.BORROWED,
    )

    borrowing.book = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        total_copies=5,
        available_copies=4,
    )

    service.borrow_repo.get.return_value = borrowing

    db = MagicMock()

    service.return_book(
        db,
        1,
    )

    assert borrowing.status == BorrowStatus.RETURNED

    db.commit.assert_called_once()


def test_already_returned(service):

    borrowing = Borrowing(
        id=1,
        status=BorrowStatus.RETURNED,
    )

    service.borrow_repo.get.return_value = borrowing

    with pytest.raises(HTTPException):

        service.return_book(
            MagicMock(),
            1,
        )


def test_borrow_record_not_found(service):

    service.borrow_repo.get.return_value = None

    with pytest.raises(HTTPException):

        service.return_book(
            MagicMock(),
            1,
        )


def test_transaction_rollback(service):

    member = Member(id=1)

    book = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        total_copies=5,
        available_copies=5,
    )

    service.member_repo.get.return_value = member

    service.book_repo.get.return_value = book

    service.borrow_repo.create.side_effect = Exception(
        "Database Failure"
    )

    db = MagicMock()

    with pytest.raises(Exception):

        service.borrow_book(
            db,
            1,
            1,
        )

    db.rollback.assert_called_once()