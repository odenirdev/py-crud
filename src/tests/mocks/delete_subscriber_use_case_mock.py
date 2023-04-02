import pytest

from src.use_cases.delete_subscriber.delete_subscriber_use_case import DeleteSubscriberUseCase


@pytest.fixture
def delete_subscriber_use_case_mock(subscribers_repository_mock):
    delete_subscriber_use_case = DeleteSubscriberUseCase(
        subscribers_repository_mock)
    return delete_subscriber_use_case
