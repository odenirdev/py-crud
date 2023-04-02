import datetime
import uuid


class Subscriber:
    def __init__(self, id=None, name=None, email=None, occupation=None, date_of_birth=None, description=None, created_at=None):
        self.name = name
        self.email = email
        self.occupation = occupation
        self.date_of_birth = date_of_birth
        self.description = description

        if id is None:
            self.id = str(uuid.uuid4())

        if created_at is None:
            self.created_at = datetime.datetime.now()
