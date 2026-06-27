from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class MemberBase(BaseModel):
    full_name: str = Field(..., min_length=2)
    email: EmailStr
    phone: str
    address: Optional[str] = None


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class MemberResponse(MemberBase):
    id: int

    model_config = ConfigDict(from_attributes=True)