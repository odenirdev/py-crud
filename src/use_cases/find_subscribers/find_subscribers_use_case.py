from src.database.connect import subscribers


class FindSubscribersUseCase:
    # def __init__(self, subscribers_repository: SubscribersRepository):
    #     self.find_subscribers_repository = find_subscribers_repository

    def execute(self):
        return subscribers
        # return self.find_subscribers_repository.find_all()
