import pytest
from fastapi import HTTPException

from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto

from src.use_cases.find_one_subscriber.find_one_subcriber_use_case import FindOneSubcriberUseCase
from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


def test_find_one_subscriber_successfully(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    subscriber = create_subscriber_use_case.execute(
        CreateSubscriberDto(name="John Doe", email="john@doe.com",
                            occupation="Software Engineer Pleno", date_of_birth="2000-01-01", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))

    find_one_subscriber_use_case = FindOneSubcriberUseCase(
        subscribers_repository_mock)

    response = find_one_subscriber_use_case.execute(
        subscriber.id)

    assert response.name is "John Doe"


def test_find_one_subscriber_not_found(subscribers_repository_mock):
    find_one_subscriber_use_case = FindOneSubcriberUseCase(
        subscribers_repository_mock)

    with pytest.raises(HTTPException) as exc:
        find_one_subscriber_use_case.execute("fake_id")

    assert exc.value.status_code == 400
    assert exc.value.detail == "Subscriber not found"
