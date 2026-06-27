from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.borrowing import (
    BorrowBookRequest,
    BorrowResponse,
    ReturnBookRequest,
)
from app.services.borrow_service import BorrowService

router = APIRouter(
    prefix="/borrowings",
    tags=["Borrowings"],
)

service = BorrowService()


@router.post(
    "",
    response_model=BorrowResponse,
)
def borrow_book(
    payload: BorrowBookRequest,
    db: Session = Depends(get_db),
):
    return service.borrow_book(
        db=db,
        member_id=payload.member_id,
        book_id=payload.book_id,
    )


@router.post(
    "/return",
    response_model=BorrowResponse,
)
def return_book(
    payload: ReturnBookRequest,
    db: Session = Depends(get_db),
):
    return service.return_book(
        db=db,
        borrowing_id=payload.borrowing_id,
    )


@router.get(
    "/member/{member_id}",
    response_model=List[BorrowResponse],
)
def borrowed_books(
    member_id: int,
    db: Session = Depends(get_db),
):
    return service.borrowed_books(
        db,
        member_id,
    )