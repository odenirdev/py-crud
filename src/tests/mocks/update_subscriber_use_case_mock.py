import pytest

from src.use_cases.update_subscriber.update_subscriber_use_case import UpdateSubscriberUseCase


@pytest.fixture
def update_subscriber_use_case_mock(subscribers_repository_mock):
    update_subscriber_use_case = UpdateSubscriberUseCase(
        subscribers_repository_mock)
    return update_subscriber_use_case
