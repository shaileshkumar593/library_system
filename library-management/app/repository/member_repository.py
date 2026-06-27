from typing import Optional

from sqlalchemy.orm import Session

from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate


class MemberRepository:

    def create(
        self,
        db: Session,
        payload: MemberCreate,
    ) -> Member:

        member = Member(**payload.model_dump())

        db.add(member)
        db.flush()
        db.refresh(member)

        return member

    def get(
        self,
        db: Session,
        member_id: int,
    ) -> Optional[Member]:

        return (
            db.query(Member)
            .filter(Member.id == member_id)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> Optional[Member]:

        return (
            db.query(Member)
            .filter(Member.email == email)
            .first()
        )

    def list(
        self,
        db: Session,
    ):

        return db.query(Member).all()

    def update(
        self,
        db: Session,
        member: Member,
        payload: MemberUpdate,
    ) -> Member:

        updates = payload.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(member, key, value)

        db.flush()
        db.refresh(member)

        return member

    def delete(
        self,
        db: Session,
        member: Member,
    ):

        db.delete(member)
        db.flush()