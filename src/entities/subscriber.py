import re
import uuid
import datetime
from fastapi import HTTPException


class Subscriber:
    def __init__(self, id=None, name=None, email=None, occupation=None, date_of_birth=None, description=None, created_at=None):
        if not name:
            raise HTTPException(
                status_code=400, detail="Subscriber name is required")

        if not email:
            raise HTTPException(
                status_code=400, detail="Subscriber email is required")
        else:
            regex = re.compile(
                r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if not regex.match(email):
                raise HTTPException(
                    status_code=400, detail="Subscriber email is not valid")

        if not occupation:
            raise HTTPException(
                status_code=400, detail="Subscriber occupation is required")

        if not date_of_birth:
            raise HTTPException(
                status_code=400, detail="Subscriber date of birth is required")

        if not description:
            raise HTTPException(
                status_code=400, detail="Subscriber description is required")

        self.name = name
        self.email = email
        self.occupation = occupation
        self.date_of_birth = date_of_birth
        self.description = description

        if id is None:
            self.id = str(uuid.uuid4())

        if created_at is None:
            self.created_at = datetime.datetime.now()
