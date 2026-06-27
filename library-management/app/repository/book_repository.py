from typing import Optional

from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class BookRepository:

    def create(
        self,
        db: Session,
        payload: BookCreate,
    ) -> Book:

        book = Book(
            title=payload.title,
            author=payload.author,
            isbn=payload.isbn,
            publisher=payload.publisher,
            published_year=payload.published_year,
            total_copies=payload.total_copies,
            available_copies=payload.total_copies,
        )

        db.add(book)
        db.flush()
        db.refresh(book)

        return book

    def get(
        self,
        db: Session,
        book_id: int,
    ) -> Optional[Book]:

        return (
            db.query(Book)
            .filter(Book.id == book_id)
            .first()
        )

    def get_by_isbn(
        self,
        db: Session,
        isbn: str,
    ) -> Optional[Book]:

        return (
            db.query(Book)
            .filter(Book.isbn == isbn)
            .first()
        )

    def list(
        self,
        db: Session,
    ):

        return db.query(Book).all()

    def update(
        self,
        db: Session,
        book: Book,
        payload: BookUpdate,
    ) -> Book:

        updates = payload.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(book, key, value)

        db.flush()
        db.refresh(book)

        return book

    def delete(
        self,
        db: Session,
        book: Book,
    ):

        db.delete(book)
        db.flush()