from fastapi import HTTPException

from src.interfaces.find_one_subscriber_response import FindOneSubscriberResponse

from src.database.mock_data import subscribers


class FindOneSubcriberUseCase:
    # def __init__(self, find_one_subscriber_repository: FindOneSubscriberRepository):
    #     self.find_one_subscriber_repository = find_one_subscriber_repository

    def execute(self, subscriber_id: str) -> FindOneSubscriberResponse:
        for subscriber in subscribers:
            if subscriber['id'] == subscriber_id:
                return {'id': subscriber['id'],
                        'name': subscriber['name'],
                        'email': subscriber['email'],
                        'occupation': subscriber['occupation'],
                        'date_of_birth': subscriber['date_of_birth'],
                        'description': subscriber['description']}

        raise HTTPException(status_code=400, detail="Item not found")
