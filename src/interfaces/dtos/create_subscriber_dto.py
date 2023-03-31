from pydantic import BaseModel


class CreateSubscriberDto(BaseModel):
    name: str
    email: str
    occupation: str
    date_of_birth: str
    description: str
