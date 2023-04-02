import pytest

from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


@pytest.fixture
def create_subscriber_use_case_mock(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)
    return create_subscriber_use_case
