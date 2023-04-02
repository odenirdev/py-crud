from fastapi import HTTPException
import pytest

from src.database.repositories.subscriber_repository import SubscriberRepository

from src.entities.subscriber_entity import SubscriberEntity

from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse
from src.interfaces.update_subscriber_response import UpdateSubscriberResponse
from src.interfaces.find_subscriber_response import FindSubscriberResponse

from src.database.mock_data import subscribers


class SubscriberRepositoryMock(SubscriberRepository):
    def find(self) -> list[FindSubscriberResponse]:
        subscribers_response = []

        for subscriber in subscribers:
            subscribers_response.append(
                FindSubscriberResponse(
                    id=subscriber.id,
                    name=subscriber.name,
                    email=subscriber.email,
                    occupation=subscriber.occupation,
                    date_of_birth=subscriber.date_of_birth,
                    description=subscriber.description,
                    created_at=subscriber.created_at))

        return subscribers_response

    def create(self, subscriber: SubscriberEntity) -> CreateSubscriberResponse:
        new_subscriber = CreateSubscriberResponse(
            id=subscriber.id,
            name=subscriber.name,
            email=subscriber.email,
            occupation=subscriber.occupation,
            date_of_birth=subscriber.date_of_birth,
            description=subscriber.description,
            created_at=subscriber.created_at.strftime("%Y-%m-%dT%H:%M")
        )

        subscribers.append(new_subscriber)

        return new_subscriber

    def find_one(self, subscriber_id: str) -> FindOneSubscriberResponse:
        for subscriber in subscribers:
            if subscriber.id == subscriber_id:
                return FindOneSubscriberResponse(
                    id=subscriber.id,
                    name=subscriber.name,
                    email=subscriber.email,
                    occupation=subscriber.occupation,
                    date_of_birth=subscriber.date_of_birth,
                    description=subscriber.description)

        raise HTTPException(status_code=400, detail="Subscriber not found")

    def delete(self, subscriber_id: str):
        subscriber_index = None
        for i in range(len(subscribers)):
            if subscribers[i].id == subscriber_id:
                subscriber_index = i
                break

        if subscriber_index is None:
            raise HTTPException(status_code=400, detail='Subscriber not found')

        subscribers.pop(subscriber_index)

    def update(self, subscriber_id: str, subscriber: SubscriberEntity):
        for subscriber_db in subscribers:
            if subscriber_db.id == subscriber_id:
                subscriber_db.name = subscriber.name
                subscriber_db.email = subscriber.email
                subscriber_db.occupation = subscriber.occupation
                subscriber_db.date_of_birth = subscriber.date_of_birth
                subscriber_db.description = subscriber.description

        return UpdateSubscriberResponse(
            id=subscriber_id,
            name=subscriber.name,
            email=subscriber.email,
            occupation=subscriber.occupation,
            date_of_birth=subscriber.date_of_birth,
            description=subscriber.description
        )


@pytest.fixture
def subscribers_repository_mock():
    subscriber_repository = SubscriberRepositoryMock()
    return subscriber_repository
