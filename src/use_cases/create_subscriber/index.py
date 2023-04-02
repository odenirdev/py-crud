from src.use_cases.create_subscriber.create_subscriber_use_case import CreateSubscriberUseCase
from src.use_cases.create_subscriber.create_subscriber_controller import CreateSubscriberController

from src.database.repositories.implementations.postgres_subscriber_repository import PostgresSubscriberRepository

postgres_subscriber_repository = PostgresSubscriberRepository()

create_subscriber_use_case = CreateSubscriberUseCase(
    postgres_subscriber_repository)

create_subscriber_controller = CreateSubscriberController(
    create_subscriber_use_case
)
