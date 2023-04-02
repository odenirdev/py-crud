from src.use_cases.find_subscribers.find_subscribers_use_case import \
    FindSubscribersUseCase


def test_find_subscribers_successfully():
    find_subscribers_use_case = FindSubscribersUseCase()

    response = find_subscribers_use_case.execute()

    assert response is not None
