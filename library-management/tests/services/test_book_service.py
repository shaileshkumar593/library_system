from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from app.models.book import Book
from app.schemas.book import BookCreate
from app.schemas.book import BookUpdate
from app.services.book_service import BookService


@pytest.fixture
def service():

    service = BookService()

    service.repo = MagicMock()

    return service


def test_create_book_success(service):

    payload = BookCreate(
        title="Python",
        author="Guido",
        isbn="123",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
    )

    service.repo.get_by_isbn.return_value = None

    service.repo.create.return_value = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
        available_copies=5,
    )

    result = service.create(None, payload)

    assert result.id == 1

    service.repo.create.assert_called_once()


def test_duplicate_isbn(service):

    payload = BookCreate(
        title="Python",
        author="Guido",
        isbn="123",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
    )

    service.repo.get_by_isbn.return_value = Book()

    with pytest.raises(HTTPException):

        service.create(None, payload)


def test_get_book(service):

    book = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
        available_copies=5,
    )

    service.repo.get.return_value = book

    result = service.get(None, 1)

    assert result.title == "Python"


def test_book_not_found(service):

    service.repo.get.return_value = None

    with pytest.raises(HTTPException):

        service.get(None, 100)


def test_update_book(service):

    payload = BookUpdate(title="Advanced Python")

    book = Book(
        id=1,
        title="Python",
        author="Guido",
        isbn="123",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
        available_copies=5,
    )

    service.repo.get.return_value = book

    service.repo.update.return_value = book

    service.update(None, 1, payload)

    service.repo.update.assert_called_once()


def test_delete_book(service):

    service.repo.get.return_value = Book()

    service.delete(None, 1)

    service.repo.delete.assert_called_once()


def test_list_books(service):

    service.repo.list.return_value = [
        Book(
            id=1,
            title="Python",
            author="Guido",
            isbn="123",
            publisher="ABC",
            published_year=2024,
            total_copies=5,
            available_copies=5,
        )
    ]

    books = service.list(None)

    assert len(books) == 1