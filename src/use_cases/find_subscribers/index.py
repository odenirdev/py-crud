from src.use_cases.find_subscribers.find_subscribers_controller import FindSubscribersController
from src.use_cases.find_subscribers.find_subscribers_use_case import FindSubscribersUseCase

from src.database.repositories.implementations.postgres_subscriber_repository import PostgresSubscriberRepository


postgres_subscriber_repository = PostgresSubscriberRepository()

find_subscribers_use_case = FindSubscribersUseCase(
    postgres_subscriber_repository)

find_subscribers_controller = FindSubscribersController(
    find_subscribers_use_case)
