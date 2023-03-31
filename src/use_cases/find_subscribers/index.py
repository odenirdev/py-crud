from src.use_cases.find_subscribers.find_subscribers_controller import FindSubscribersController
from src.use_cases.find_subscribers.find_subscribers_use_case import FindSubscribersUseCase


find_subscribers_use_case = FindSubscribersUseCase()

find_subscribers_controller = FindSubscribersController(
    find_subscribers_use_case)
