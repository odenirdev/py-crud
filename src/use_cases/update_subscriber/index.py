from src.use_cases.update_subscriber.update_subscriber_controller import UpdateSubscriberController
from src.use_cases.update_subscriber.update_subscriber_use_case import UpdateSubscriberUseCase


update_subscriber_use_case = UpdateSubscriberUseCase(
)

update_subscriber_controller = UpdateSubscriberController(
    update_subscriber_use_case)
