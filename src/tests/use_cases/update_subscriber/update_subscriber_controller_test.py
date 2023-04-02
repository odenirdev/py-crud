from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto

from src.use_cases.update_subscriber.update_subscriber_controller import UpdateSubscriberController
from src.use_cases.create_subscriber.create_subscriber_controller import CreateSubscriberController


def test_update_subscriber_successfully(update_subscriber_use_case_mock, create_subscriber_use_case_mock):
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

    update_subscriber_controller = UpdateSubscriberController(
        update_subscriber_use_case_mock)

    response = update_subscriber_controller.execute(
        subscriber.id, UpdateSubscriberDto(
            occupation="Software Engineer Senior"
        )
    )

    assert response.occupation == "Software Engineer Senior"
