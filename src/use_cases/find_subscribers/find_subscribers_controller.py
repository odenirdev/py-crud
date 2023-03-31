from src.use_cases.find_subscribers.find_subscribers_use_case import FindSubscribersUseCase


class FindSubscribersController:

    def __init__(self, find_subscribers_use_case: FindSubscribersUseCase):
        self.find_subscribers_use_case = find_subscribers_use_case

    def execute(self):
        return self.find_subscribers_use_case.execute()
