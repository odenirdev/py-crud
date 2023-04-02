import pytest
from fastapi import HTTPException

from src.interfaces.update_subscriber_response import UpdateSubscriberResponse
from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto

from src.database.mock_data import subscribers


class UpdateSubscriberUseCase:
    def execute(self, subscriber_id: str, update_subscriber_dto: UpdateSubscriberDto) -> UpdateSubscriberResponse:
        subscriber_index = None
        for i in range(len(subscribers)):
            if subscribers[i].id == subscriber_id:
                subscriber_index = i
                break

        if subscriber_index is None:
            raise HTTPException(status_code=400, detail='Subscriber not found')

        if update_subscriber_dto.name is not None:
            subscribers[subscriber_index].name = update_subscriber_dto.name

        if update_subscriber_dto.email is not None:
            subscribers[subscriber_index].email = update_subscriber_dto.email

        if update_subscriber_dto.occupation is not None:
            subscribers[subscriber_index].occupation = update_subscriber_dto.occupation

        if update_subscriber_dto.date_of_birth is not None:
            subscribers[subscriber_index].date_of_birth = update_subscriber_dto.date_of_birth

        if update_subscriber_dto.description is not None:
            subscribers[subscriber_index].description = update_subscriber_dto.description

        return subscribers[subscriber_index]


@pytest.fixture
def update_subscriber_use_case_mock():
    update_subscriber_use_case = UpdateSubscriberUseCase()
    return update_subscriber_use_case
