from src.use_cases.delete_subscriber.delete_subscriber_use_case import DeleteSubscriberUseCase


class DeleteSubscriberController:
    def __init__(self, delete_subscriber_use_case: DeleteSubscriberUseCase) -> None:
        self.delete_subscriber_use_case = delete_subscriber_use_case

    def execute(self, subscriber_id: str) -> None:
        return self.delete_subscriber_use_case.execute(subscriber_id)
