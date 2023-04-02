from fastapi import HTTPException

from src.database.repositories.subscriber_repository import SubscriberRepository

from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto

from src.entities.subscriber import Subscriber


class CreateSubscriberUseCase:
    def __init__(self, subscriber_repository: SubscriberRepository):
        self.subscriber_repository = subscriber_repository

    def execute(self, create_subscriber_dto: CreateSubscriberDto) -> CreateSubscriberResponse:
        subscriber = Subscriber(
            name=create_subscriber_dto.name,
            email=create_subscriber_dto.email,
            occupation=create_subscriber_dto.occupation,
            date_of_birth=create_subscriber_dto.date_of_birth,
            description=create_subscriber_dto.description
        )

        return self.subscriber_repository.create(subscriber)
