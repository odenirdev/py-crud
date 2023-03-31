from fastapi import HTTPException

from src.database.connect import subscribers


class DeleteSubscriberUseCase:
    def execute(self, subscriber_id: str) -> None:
        subscriber_index = None
        for i in range(len(subscribers)):
            if subscribers[i]['id'] == subscriber_id:
                subscriber_index = i
                break

        if subscriber_index is None:
            raise HTTPException(status_code=400, detail='Subscriber not found')

        subscribers.pop(subscriber_index)
