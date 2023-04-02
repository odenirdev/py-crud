import pytest

from src.use_cases.find_subscribers.find_subscribers_use_case import \
    FindSubscribersUseCase


@pytest.fixture
def find_subscribers_use_case_mock(subscribers_repository_mock):
    find_subscribers_use_case = FindSubscribersUseCase(
        subscribers_repository_mock)
    return find_subscribers_use_case
