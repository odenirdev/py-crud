from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto

from src.use_cases.find_one_subscriber.find_one_subcriber_controller import FindOneSubscriberController
from src.use_cases.create_subscriber.create_subscriber_controller import CreateSubscriberController


def test_find_one_subscriber_successfully(find_one_subscriber_use_case_mock, create_subscriber_use_case_mock):
    create_subscriber_controller = CreateSubscriberController(
        create_subscriber_use_case_mock)

    subscriber = create_subscriber_controller.execute(
        CreateSubscriberDto(
            name="John Doe",
            email="john@doe.com",
            occupation="Software Engineer",
            date_of_birth="2000-01-01",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        )
    )

    find_one_subscriber_controller = FindOneSubscriberController(
        find_one_subscriber_use_case_mock
    )

    response = find_one_subscriber_controller.execute(
        subscriber.id)

    assert response.id is subscriber.id
