from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.database import Base


class BorrowStatus(str, Enum):
    BORROWED = "BORROWED"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class Borrowing(Base):
    __tablename__ = "borrowings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    member_id: Mapped[int] = mapped_column(
        ForeignKey("members.id", ondelete="CASCADE"),
        nullable=False,
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False,
    )

    borrow_date: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    due_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    return_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    status: Mapped[BorrowStatus] = mapped_column(
        SqlEnum(BorrowStatus),
        default=BorrowStatus.BORROWED,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    member = relationship(
        "Member",
        back_populates="borrowings",
    )

    book = relationship(
        "Book",
        back_populates="borrowings",
    )