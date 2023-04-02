from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto

from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


def test_create_subscriber_successfully(subscribers_repository_mock):
    create_subscriber_use_case = CreateSubscriberUseCase(
        subscribers_repository_mock)

    new_subscriber = CreateSubscriberDto(
        name="John Doe",
        email="john@doe.com",
        occupation="Software Engineer",
        date_of_birth="2000-01-01",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    response = create_subscriber_use_case.execute(new_subscriber)

    assert response.id is not None
