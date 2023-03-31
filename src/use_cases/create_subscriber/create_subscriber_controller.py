from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase


class CreateSubscriberController:
    def __init__(self, create_subscriber_use_case: CreateSubscriberUseCase):
        self.create_subscriber_use_case = create_subscriber_use_case

    def execute(self, create_subscriber_dto: CreateSubscriberDto):
        return self.create_subscriber_use_case.execute(create_subscriber_dto)
