import pytest
from fastapi import HTTPException

from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto

from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


def test_create_subscriber_successfully(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    new_subscriber = CreateSubscriberDto(
        name="John Doe",
        email="john@doe.com",
        occupation="Software Engineer",
        date_of_birth="2000-01-01",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    response = create_subscriber_use_case.execute(new_subscriber)

    assert response.id is not None


def test_required_fields_are_not_provided(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    new_subscriber = CreateSubscriberDto(
        name="John Doe",
        email="",
        occupation="Software Engineer",
        date_of_birth="2000-01-01",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    with pytest.raises(HTTPException) as exc:
        create_subscriber_use_case.execute(new_subscriber)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Subscriber email is required"


def test_invalid_email_is_provided(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    new_subscriber = CreateSubscriberDto(
        name="John Doe",
        email="john@doe",
        occupation="Software Engineer",
        date_of_birth="2000-01-01",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    with pytest.raises(HTTPException) as exc:
        create_subscriber_use_case.execute(new_subscriber)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Subscriber email is not valid"
