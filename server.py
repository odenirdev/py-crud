from fastapi import FastAPI
import uvicorn

from src.interfaces.dtos.create_subscriber_dto import CreateSubscriberDto
from src.interfaces.create_subscriber_response import CreateSubscriberResponse
from src.interfaces.find_subscriber_response import FindSubscriberResponse

from src.use_cases.find_subscribers.index import find_subscribers_controller
from src.use_cases.create_subscriber.index import create_subscriber_controller


app = FastAPI()


@app.get('/subscriber')
def get_subscribers() -> list[FindSubscriberResponse]:
    return find_subscribers_controller.execute()


@app.post('/subscriber')
def post_subscribers(create_subscriber_dto: CreateSubscriberDto) -> CreateSubscriberResponse:
    return create_subscriber_controller.execute(create_subscriber_dto)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
