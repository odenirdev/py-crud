import pytest
from fastapi import HTTPException

from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto

from src.use_cases.update_subscriber.update_subscriber_use_case import UpdateSubscriberUseCase
from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


def test_update_subscriber_successfully(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    subscriber = create_subscriber_use_case.execute(
        CreateSubscriberDto(name="John Doe", email="john@doe.com",
                            occupation="Software Engineer Pleno", date_of_birth="2000-01-01", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))

    update_subscriber_use_case = UpdateSubscriberUseCase(
        subscribers_repository_mock)

    response = update_subscriber_use_case.execute(
        subscriber.id, UpdateSubscriberDto(
            occupation="Software Engineer Senior")
    )

    assert response.occupation == "Software Engineer Senior"


def test_update_subscriber_not_found(subscribers_repository_mock):
    update_subscriber_use_case = UpdateSubscriberUseCase(
        subscribers_repository_mock)

    with pytest.raises(HTTPException) as exc:
        update_subscriber_use_case.execute("fake_id", UpdateSubscriberDto(
            occupation="Software Engineer Pleno"))

    assert exc.value.status_code == 400
    assert exc.value.detail == "Subscriber not found"
