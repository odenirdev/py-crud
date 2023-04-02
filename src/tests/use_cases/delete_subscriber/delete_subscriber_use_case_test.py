from fastapi import HTTPException
import pytest
from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto


from src.use_cases.delete_subscriber.delete_subscriber_use_case import DeleteSubscriberUseCase
from src.use_cases.find_one_subscriber.find_one_subcriber_use_case import FindOneSubcriberUseCase
from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


def test_delete_subscriber_successfully():
    create_subscriber_use_case = CreateSubscriberUseCase()

    subscriber = create_subscriber_use_case.execute(
        CreateSubscriberDto(name="John Doe", email="john@doe.com",
                            occupation="Software Engineer Pleno", date_of_birth="2000-01-01", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))

    find_one_subscriber_use_case = FindOneSubcriberUseCase()

    find_subscriber = find_one_subscriber_use_case.execute(subscriber.id)

    assert find_subscriber.id is not None

    print(find_subscriber)

    delete_subscriber_use_case = DeleteSubscriberUseCase()

    delete_subscriber_use_case.execute(find_subscriber.id)

    with pytest.raises(HTTPException) as exc:
        find_one_subscriber_use_case.execute(subscriber.id)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Subscriber not found"
