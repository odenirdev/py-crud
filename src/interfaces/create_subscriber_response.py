from pydantic import BaseModel


class CreateSubscriberResponse(BaseModel):
    id: str
    name: str
    email: str
    occupation: str
    date_of_birth: str
    description: str
