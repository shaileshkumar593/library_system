from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services.book_service import BookService

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)

service = BookService()


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    payload: BookCreate,
    db: Session = Depends(get_db),
):
    return service.create(db, payload)


@router.get(
    "",
    response_model=List[BookResponse],
)
def get_books(
    db: Session = Depends(get_db),
):
    return service.list(db)


@router.get(
    "/{book_id}",
    response_model=BookResponse,
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    return service.get(db, book_id)


@router.put(
    "/{book_id}",
    response_model=BookResponse,
)
def update_book(
    book_id: int,
    payload: BookUpdate,
    db: Session = Depends(get_db),
):
    return service.update(db, book_id, payload)


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    service.delete(db, book_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)