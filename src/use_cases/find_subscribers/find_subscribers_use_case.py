from src.database.repositories.subscriber_repository import SubscriberRepository

from src.interfaces.find_subscriber_response import FindSubscriberResponse


class FindSubscribersUseCase:
    def __init__(self, subscribers_repository: SubscriberRepository):
        self.subscribers_repository = subscribers_repository

    def execute(self) -> list[FindSubscriberResponse]:
        return self.subscribers_repository.find()
