from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.member import MemberCreate, MemberResponse, MemberUpdate
from app.services.member_service import MemberService

router = APIRouter(
    prefix="/members",
    tags=["Members"],
)

service = MemberService()


@router.post(
    "",
    response_model=MemberResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_member(
    payload: MemberCreate,
    db: Session = Depends(get_db),
):
    return service.create(db, payload)


@router.get(
    "",
    response_model=List[MemberResponse],
)
def get_members(
    db: Session = Depends(get_db),
):
    return service.list(db)


@router.get(
    "/{member_id}",
    response_model=MemberResponse,
)
def get_member(
    member_id: int,
    db: Session = Depends(get_db),
):
    return service.get(db, member_id)


@router.put(
    "/{member_id}",
    response_model=MemberResponse,
)
def update_member(
    member_id: int,
    payload: MemberUpdate,
    db: Session = Depends(get_db),
):
    return service.update(db, member_id, payload)


@router.delete(
    "/{member_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_member(
    member_id: int,
    db: Session = Depends(get_db),
):
    service.delete(db, member_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)