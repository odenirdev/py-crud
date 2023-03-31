from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.database.mock_data import subscribers

from uuid import uuid4


class CreateSubscriberUseCase:
    def execute(self, create_subscriber_dto: CreateSubscriberDto) -> CreateSubscriberResponse:
        created_subscriber = {
            "id": str(uuid4()),
            "name": create_subscriber_dto.name,
            "email": create_subscriber_dto.email,
            "occupation": create_subscriber_dto.occupation,
            "date_of_birth": create_subscriber_dto.date_of_birth,
            "description": create_subscriber_dto.description
        }

        subscribers.append(created_subscriber)

        return created_subscriber
