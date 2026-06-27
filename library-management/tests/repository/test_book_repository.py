from app.repository.book_repository import BookRepository
from app.schemas.book import BookCreate, BookUpdate


repo = BookRepository()


def test_create_book(db):

    payload = BookCreate(
        title="Python",
        author="Guido",
        isbn="ISBN-100",
        publisher="ABC",
        published_year=2024,
        total_copies=5,
    )

    book = repo.create(db, payload)

    db.commit()

    assert book.id is not None
    assert book.title == "Python"
    assert book.available_copies == 5


def test_get_book(db, sample_book):

    book = repo.get(db, sample_book.id)

    assert book is not None
    assert book.title == "Clean Code"


def test_get_invalid_book(db):

    book = repo.get(db, 9999)

    assert book is None


def test_get_by_isbn(db, sample_book):

    book = repo.get_by_isbn(
        db,
        sample_book.isbn,
    )

    assert book is not None
    assert book.author == "Robert C. Martin"


def test_list_books(db, multiple_books):

    books = repo.list(db)

    assert len(books) == 5


def test_update_book(db, sample_book):

    payload = BookUpdate(
        title="Advanced Python",
        total_copies=20,
    )

    updated = repo.update(
        db,
        sample_book,
        payload,
    )

    db.commit()

    assert updated.title == "Advanced Python"
    assert updated.total_copies == 20


def test_delete_book(db, sample_book):

    repo.delete(
        db,
        sample_book,
    )

    db.commit()

    deleted = repo.get(
        db,
        sample_book.id,
    )

    assert deleted is None