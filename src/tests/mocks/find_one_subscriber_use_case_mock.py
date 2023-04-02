import pytest

from src.use_cases.find_one_subscriber.find_one_subcriber_use_case import FindOneSubcriberUseCase


@ pytest.fixture
def find_one_subscriber_use_case_mock(subscribers_repository_mock):
    find_one_subscriber_use_case = FindOneSubcriberUseCase(
        subscribers_repository_mock)
    return find_one_subscriber_use_case
