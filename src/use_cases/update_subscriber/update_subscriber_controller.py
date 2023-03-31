from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto
from src.interfaces.update_subscriber_response import UpdateSubscriberResponse

from src.use_cases.update_subscriber.update_subscriber_use_case import UpdateSubscriberUseCase


class UpdateSubscriberController:
    def __init__(self, update_subscriber_use_case: UpdateSubscriberUseCase) -> None:
        self.update_subscriber_use_case = update_subscriber_use_case

    def execute(self, subscriber_id: str, update_subscriber_dto: UpdateSubscriberDto) -> UpdateSubscriberResponse:
        return self.update_subscriber_use_case.execute(
            subscriber_id, update_subscriber_dto)
