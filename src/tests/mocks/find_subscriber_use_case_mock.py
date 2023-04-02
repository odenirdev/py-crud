import pytest

from src.database.mock_data import subscribers
from src.use_cases.find_subscribers.find_subscribers_use_case import \
    FindSubscribersUseCase


class FindSubscribersUseCaseMock(FindSubscribersUseCase):
    def execute(self):
        return subscribers


@pytest.fixture
def find_subscribers_use_case_mock():
    find_subscribers_use_case = FindSubscribersUseCaseMock()
    return find_subscribers_use_case
