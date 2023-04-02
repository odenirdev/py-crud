from src.use_cases.find_subscribers.find_subscribers_controller import \
    FindSubscribersController


def test_find_subscribers_successfully(find_subscribers_use_case_mock):
    find_subscribers_controller = FindSubscribersController(
        find_subscribers_use_case_mock)

    response = find_subscribers_controller.execute()

    assert response is not None
