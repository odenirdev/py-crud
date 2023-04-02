from fastapi import HTTPException

from src.database.repositories.subscriber_repository import SubscriberRepository

from src.database.mock_data import subscribers


class DeleteSubscriberUseCase:
    def __init__(self, subscribers_repository: SubscriberRepository):
        self.subscribers_repository = subscribers_repository

    def execute(self, subscriber_id: str) -> None:
        self.subscribers_repository.delete(subscriber_id)
