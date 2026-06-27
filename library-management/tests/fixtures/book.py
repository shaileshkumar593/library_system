import pytest

from app.models.book import Book


@pytest.fixture
def sample_book(db):

    book = Book(
        title="Clean Code",
        author="Robert C. Martin",
        isbn="9780132350884",
        publisher="Pearson",
        published_year=2008,
        total_copies=5,
        available_copies=5,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


@pytest.fixture
def multiple_books(db):

    books = []

    for i in range(5):

        book = Book(
            title=f"Book {i}",
            author=f"Author {i}",
            isbn=f"ISBN-{i}",
            publisher="ABC",
            published_year=2024,
            total_copies=10,
            available_copies=10,
        )

        db.add(book)

        books.append(book)

    db.commit()

    return books