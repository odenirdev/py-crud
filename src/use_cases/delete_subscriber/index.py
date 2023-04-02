from src.use_cases.delete_subscriber.delete_subscriber_use_case import DeleteSubscriberUseCase
from src.use_cases.delete_subscriber.delete_subscriber_controller import DeleteSubscriberController

from src.database.repositories.implementations.postgres_subscriber_repository import PostgresSubscriberRepository


postgres_subscriber_repository = PostgresSubscriberRepository()

delete_subscriber_use_case = DeleteSubscriberUseCase(
    postgres_subscriber_repository
)


delete_subscriber_controller = DeleteSubscriberController(
    delete_subscriber_use_case
)
