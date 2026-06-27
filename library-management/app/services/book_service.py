from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repository.book_repository import BookRepository
from app.schemas.book import BookCreate
from app.schemas.book import BookUpdate


class BookService:

    def __init__(self):
        self.repo = BookRepository()

    def create(
        self,
        db: Session,
        payload: BookCreate,
    ):

        existing = self.repo.get_by_isbn(
            db,
            payload.isbn,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Book already exists",
            )

        return self.repo.create(
            db,
            payload,
        )

    def get(
        self,
        db: Session,
        book_id: int,
    ):

        book = self.repo.get(
            db,
            book_id,
        )

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        return book

    def list(
        self,
        db: Session,
    ):
        return self.repo.list(db)

    def update(
        self,
        db: Session,
        book_id: int,
        payload: BookUpdate,
    ):

        book = self.get(
            db,
            book_id,
        )

        return self.repo.update(
            db,
            book,
            payload,
        )

    def delete(
        self,
        db: Session,
        book_id: int,
    ):

        book = self.get(
            db,
            book_id,
        )

        self.repo.delete(
            db,
            book,
        )