from fastapi import HTTPException

from src.database.repositories.subscriber_repository import SubscriberRepository

from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto
from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse
from src.interfaces.find_subscriber_response import FindSubscriberResponse
from src.interfaces.update_subscriber_response import UpdateSubscriberResponse

from src.entities.subscriber_entity import SubscriberEntity

from src.database.mock_data import subscribers

from src.database.session import session, Subscriber


class PostgresSubscriberRepository(SubscriberRepository):
    def find(self) -> list[FindSubscriberResponse]:
        response_subscribers = session.query(Subscriber).all()

        subscribers = []
        for subscriber in response_subscribers:
            subscribers.append(
                FindSubscriberResponse(
                    id=subscriber.id,
                    name=subscriber.name,
                    email=subscriber.email,
                    occupation=subscriber.occupation,
                    date_of_birth=subscriber.date_of_birth,
                    description=subscriber.description,
                    created_at=subscriber.created_at))

        return subscribers

    def create(self, subscriber_entity: SubscriberEntity) -> CreateSubscriberResponse:
        subscriber = Subscriber(
            id=subscriber_entity.id,
            name=subscriber_entity.name,
            email=subscriber_entity.email,
            occupation=subscriber_entity.occupation,
            date_of_birth=subscriber_entity.date_of_birth,
            description=subscriber_entity.description,
            created_at=subscriber_entity.created_at.strftime("%Y-%m-%dT%H:%M"))

        session.add(subscriber)
        session.commit()

        return CreateSubscriberResponse(
            id=subscriber.id,
            name=subscriber.name,
            email=subscriber.email,
            occupation=subscriber.occupation,
            date_of_birth=subscriber.date_of_birth,
            description=subscriber.description,
            created_at=subscriber.created_at
        )

    def find_one(self, subscriber_id: str) -> FindOneSubscriberResponse:
        subscriber = session.query(Subscriber).filter_by(
            id=subscriber_id).first()

        if subscriber is None:
            raise HTTPException(status_code=400, detail="Subscriber not found")

        return FindOneSubscriberResponse(
            id=subscriber.id,
            name=subscriber.name,
            email=subscriber.email,
            occupation=subscriber.occupation,
            date_of_birth=subscriber.date_of_birth,
            description=subscriber.description,
            created_at=subscriber.created_at
        )

    def delete(self, subscriber_id: str):
        subscriber = session.query(Subscriber).filter_by(
            id=subscriber_id).first()

        if subscriber is None:
            raise HTTPException(status_code=400, detail="Subscriber not found")

        session.delete(subscriber)
        session.commit()

    def update(self, subscriber_id: str, subscriber_entity: SubscriberEntity):
        subscriber_db = session.query(Subscriber).filter_by(
            id=subscriber_id).first()

        if subscriber_db is None:
            raise HTTPException(status_code=400, detail="Subscriber not found")

        subscriber_db.name = subscriber_entity.name
        subscriber_db.email = subscriber_entity.email
        subscriber_db.occupation = subscriber_entity.occupation
        subscriber_db.date_of_birth = subscriber_entity.date_of_birth
        subscriber_db.description = subscriber_entity.description

        session.commit()

        return UpdateSubscriberResponse(
            id=subscriber_id,
            name=subscriber_db.name,
            email=subscriber_db.email,
            occupation=subscriber_db.occupation,
            date_of_birth=subscriber_db.date_of_birth,
            description=subscriber_db.description
        )
