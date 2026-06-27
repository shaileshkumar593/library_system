from datetime import datetime
from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.borrowing import BorrowStatus
from app.repository.book_repository import BookRepository
from app.repository.borrowing_repository import BorrowRepository
from app.repository.member_repository import MemberRepository


class BorrowService:

    def __init__(self):

        self.book_repo = BookRepository()

        self.member_repo = MemberRepository()

        self.borrow_repo = BorrowRepository()

    def borrow_book(
        self,
        db: Session,
        member_id: int,
        book_id: int,
    ):

        member = self.member_repo.get(
            db,
            member_id,
        )

        if not member:
            raise HTTPException(
                404,
                "Member not found",
            )

        book = self.book_repo.get(
            db,
            book_id,
        )

        if not book:
            raise HTTPException(
                404,
                "Book not found",
            )

        if book.available_copies <= 0:
            raise HTTPException(
                400,
                "Book unavailable",
            )

        try:

            borrowing = self.borrow_repo.create(
                db=db,
                member_id=member_id,
                book_id=book_id,
                due_date=datetime.utcnow() + timedelta(days=14),
            )

            book.available_copies -= 1

            db.commit()

            db.refresh(book)

            return borrowing

        except Exception:

            db.rollback()

            raise

    def return_book(
        self,
        db: Session,
        borrowing_id: int,
    ):

        borrowing = self.borrow_repo.get(
            db,
            borrowing_id,
        )

        if not borrowing:
            raise HTTPException(
                404,
                "Borrow record not found",
            )

        if borrowing.status == BorrowStatus.RETURNED:
            raise HTTPException(
                400,
                "Book already returned",
            )

        try:

            borrowing.status = BorrowStatus.RETURNED

            borrowing.return_date = datetime.utcnow()

            borrowing.book.available_copies += 1

            db.commit()

            db.refresh(borrowing)

            return borrowing

        except Exception:

            db.rollback()

            raise

    def borrowed_books(
        self,
        db: Session,
        member_id: int,
    ):

        return self.borrow_repo.get_active_by_member(
            db,
            member_id,
        )