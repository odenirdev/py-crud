import uvicorn
from fastapi import FastAPI

from src.interfaces.dtos.update_subscriber_dto import UpdateSubscriberDto
from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.find_subscriber_response import FindSubscriberResponse
from src.interfaces.update_subscriber_response import UpdateSubscriberResponse

from src.use_cases.find_subscribers.index import find_subscribers_controller
from src.use_cases.create_subscriber.index import create_subscriber_controller
from src.use_cases.find_one_subscriber.index import find_one_subscriber_controller
from src.use_cases.update_subscriber.index import update_subscriber_controller
from src.use_cases.delete_subscriber.index import delete_subscriber_controller


app = FastAPI()


@app.get('/subscriber')
def get_subscribers() -> list[FindSubscriberResponse]:
    return find_subscribers_controller.execute()


@app.post('/subscriber')
def post_subscribers(create_subscriber_dto: CreateSubscriberDto) -> CreateSubscriberResponse:
    return create_subscriber_controller.execute(create_subscriber_dto)


@app.get('/subscriber/{subscriber_id}')
def get_find_one_subscriber(subscriber_id: str) -> CreateSubscriberResponse:
    return find_one_subscriber_controller.execute(subscriber_id)


@app.put('/subscriber/{subscriber_id}')
def put_update_subscriber(subscriber_id: str, update_subscriber_dto: UpdateSubscriberDto) -> UpdateSubscriberResponse:
    return update_subscriber_controller.execute(subscriber_id, update_subscriber_dto)


@app.delete('/subscriber/{subscriber_id}')
def delete_subscriber(subscriber_id: str) -> None:
    return delete_subscriber_controller.execute(subscriber_id)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
