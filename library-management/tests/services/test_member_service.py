from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from app.models.member import Member
from app.schemas.member import MemberCreate
from app.schemas.member import MemberUpdate
from app.services.member_service import MemberService


@pytest.fixture
def service():

    service = MemberService()

    service.repo = MagicMock()

    return service


def test_create_member(service):

    payload = MemberCreate(
        full_name="John",
        email="john@test.com",
        phone="999999999",
        address="USA",
    )

    service.repo.get_by_email.return_value = None

    service.repo.create.return_value = Member(
        id=1,
        full_name="John",
        email="john@test.com",
        phone="999999999",
        address="USA",
    )

    member = service.create(None, payload)

    assert member.id == 1


def test_duplicate_email(service):

    service.repo.get_by_email.return_value = Member()

    payload = MemberCreate(
        full_name="John",
        email="john@test.com",
        phone="999999999",
        address="USA",
    )

    with pytest.raises(HTTPException):

        service.create(None, payload)


def test_member_not_found(service):

    service.repo.get.return_value = None

    with pytest.raises(HTTPException):

        service.get(None, 100)


def test_update_member(service):

    member = Member(
        id=1,
        full_name="John",
        email="john@test.com",
        phone="999",
        address="USA",
    )

    service.repo.get.return_value = member

    service.repo.update.return_value = member

    service.update(
        None,
        1,
        MemberUpdate(full_name="Jane"),
    )

    service.repo.update.assert_called_once()


def test_delete_member(service):

    service.repo.get.return_value = Member()

    service.delete(None, 1)

    service.repo.delete.assert_called_once()