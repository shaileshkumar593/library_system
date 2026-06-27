from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repository.member_repository import MemberRepository
from app.schemas.member import MemberCreate
from app.schemas.member import MemberUpdate


class MemberService:

    def __init__(self):

        self.repo = MemberRepository()

    def create(
        self,
        db: Session,
        payload: MemberCreate,
    ):

        if self.repo.get_by_email(
            db,
            payload.email,
        ):
            raise HTTPException(
                409,
                "Email already exists",
            )

        return self.repo.create(
            db,
            payload,
        )

    def get(
        self,
        db: Session,
        member_id: int,
    ):

        member = self.repo.get(
            db,
            member_id,
        )

        if not member:
            raise HTTPException(
                404,
                "Member not found",
            )

        return member

    def list(
        self,
        db: Session,
    ):

        return self.repo.list(db)

    def update(
        self,
        db: Session,
        member_id: int,
        payload: MemberUpdate,
    ):

        member = self.get(
            db,
            member_id,
        )

        return self.repo.update(
            db,
            member,
            payload,
        )

    def delete(
        self,
        db: Session,
        member_id: int,
    ):

        member = self.get(
            db,
            member_id,
        )

        self.repo.delete(
            db,
            member,
        )