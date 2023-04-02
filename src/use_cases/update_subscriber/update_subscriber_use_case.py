from fastapi import HTTPException

from src.database.repositories.subscriber_repository import SubscriberRepository
from src.entities.subscriber_entity import SubscriberEntity

from src.interfaces.update_subscriber_response import UpdateSubscriberResponse
from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto

from src.database.mock_data import subscribers


class UpdateSubscriberUseCase:
    def __init__(self, subscribers_repository: SubscriberRepository):
        self.subscribers_repository = subscribers_repository
        #     self.find_one_subscriber_use_case = find_one_subscriber_use_case
        # update_subscriber_repository: UpdateSubscriberRepository
        # self.update_subscriber_repository = update_subscriber_repository

    def execute(self, subscriber_id: str, update_subscriber_dto: UpdateSubscriberDto) -> UpdateSubscriberResponse:
        update_subscriber = self.subscribers_repository.find_one(subscriber_id)

        if update_subscriber_dto.name:
            update_subscriber.name = update_subscriber_dto.name

        if update_subscriber_dto.email:
            update_subscriber.email = update_subscriber_dto.email

        if update_subscriber_dto.occupation:
            update_subscriber.occupation = update_subscriber_dto.occupation

        if update_subscriber_dto.date_of_birth:
            update_subscriber.date_of_birth = update_subscriber_dto.date_of_birth

        if update_subscriber_dto.description:
            update_subscriber.description = update_subscriber_dto.description

        subscriber = SubscriberEntity(
            id=subscriber_id,
            name=update_subscriber.name,
            email=update_subscriber.email,
            occupation=update_subscriber.occupation,
            date_of_birth=update_subscriber.date_of_birth,
            description=update_subscriber.description)

        return self.subscribers_repository.update(subscriber_id, subscriber)
