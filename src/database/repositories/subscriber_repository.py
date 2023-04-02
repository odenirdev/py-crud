from src.entities.subscriber import Subscriber

from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse
from src.interfaces.update_subscriber_response import UpdateSubscriberResponse


class SubscriberRepository:
    def find(self):
        pass

    def create(self, subscriber: Subscriber) -> CreateSubscriberResponse:
        pass

    def find_one(self, subscriber_id: str) -> FindOneSubscriberResponse:
        pass

    def delete(self, subscriber_id: str):
        pass

    def update(self, subscriber_id: str, subscriber: Subscriber) -> UpdateSubscriberResponse:
        pass
