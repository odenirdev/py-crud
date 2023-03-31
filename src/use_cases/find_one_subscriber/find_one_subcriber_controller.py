from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse


class FindOneSubscriberController:
    def __init__(self, find_one_subscriber_use_case):
        self.find_one_subscriber_use_case = find_one_subscriber_use_case

    def execute(self, subscriber_id: str) -> FindOneSubscriberResponse:
        return self.find_one_subscriber_use_case.execute(subscriber_id)
