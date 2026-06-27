from datetime import datetime

from sqlalchemy.orm import Session

from app.models.borrowing import BorrowStatus, Borrowing


class BorrowRepository:

    def create(
        self,
        db: Session,
        member_id: int,
        book_id: int,
        due_date: datetime,
    ) -> Borrowing:

        borrowing = Borrowing(
            member_id=member_id,
            book_id=book_id,
            due_date=due_date,
            status=BorrowStatus.BORROWED,
        )

        db.add(borrowing)
        db.flush()
        db.refresh(borrowing)

        return borrowing

    def get(
        self,
        db: Session,
        borrowing_id: int,
    ) -> Borrowing | None:

        return (
            db.query(Borrowing)
            .filter(Borrowing.id == borrowing_id)
            .first()
        )

    def list(
        self,
        db: Session,
    ):

        return db.query(Borrowing).all()

    def get_active_by_member(
        self,
        db: Session,
        member_id: int,
    ):

        return (
            db.query(Borrowing)
            .filter(
                Borrowing.member_id == member_id,
                Borrowing.status == BorrowStatus.BORROWED,
            )
            .all()
        )

    def update_status(
        self,
        db: Session,
        borrowing: Borrowing,
        status: BorrowStatus,
        return_date: datetime | None = None,
    ) -> Borrowing:

        borrowing.status = status
        borrowing.return_date = return_date

        db.flush()
        db.refresh(borrowing)

        return borrowing

    def delete(
        self,
        db: Session,
        borrowing: Borrowing,
    ):

        db.delete(borrowing)
        db.flush()