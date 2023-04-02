from fastapi import HTTPException

from src.database.repositories.subscriber_repository import SubscriberRepository

from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse

from src.database.mock_data import subscribers


class FindOneSubcriberUseCase:
    def __init__(self, subscribers_repository: SubscriberRepository):
        self.subscribers_repository = subscribers_repository

    def execute(self, subscriber_id: str) -> FindOneSubscriberResponse:
        return self.subscribers_repository.find_one(subscriber_id)
