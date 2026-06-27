from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.borrowing import BorrowStatus


class BorrowBookRequest(BaseModel):
    member_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)


class ReturnBookRequest(BaseModel):
    borrowing_id: int = Field(..., gt=0)


class BorrowResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    borrow_date: datetime
    due_date: datetime
    return_date: Optional[datetime]
    status: BorrowStatus

    model_config = ConfigDict(from_attributes=True)

