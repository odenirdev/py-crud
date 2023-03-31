from src.use_cases.delete_subscriber.delete_subscriber_use_case import DeleteSubscriberUseCase
from src.use_cases.delete_subscriber.delete_subscriber_controller import DeleteSubscriberController


delete_subscriber_use_case = DeleteSubscriberUseCase(

)


delete_subscriber_controller = DeleteSubscriberController(
    delete_subscriber_use_case
)
