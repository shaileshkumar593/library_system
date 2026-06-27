from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    isbn: str = Field(..., max_length=30)
    publisher: Optional[str] = None
    published_year: Optional[int] = None
    total_copies: int = Field(..., gt=0)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    published_year: Optional[int] = None
    total_copies: Optional[int] = Field(default=None, gt=0)


class BookResponse(BookBase):
    id: int
    available_copies: int

    model_config = ConfigDict(from_attributes=True)