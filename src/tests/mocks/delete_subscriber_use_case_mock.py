from fastapi import HTTPException
import pytest

from src.database.mock_data import subscribers


class DeleteSubscriberUseCase:
    def execute(self, subscriber_id: str) -> None:
        subscriber_index = None
        for i in range(len(subscribers)):
            if subscribers[i].id == subscriber_id:
                subscriber_index = i
                break

        if subscriber_index is None:
            raise HTTPException(status_code=400, detail='Subscriber not found')

        subscribers.pop(subscriber_index)


@pytest.fixture
def delete_subscriber_use_case_mock():
    delete_subscriber_use_case = DeleteSubscriberUseCase()
    return delete_subscriber_use_case
