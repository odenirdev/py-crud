from pydantic import BaseModel


class FindOneSubscriberResponse(BaseModel):
    id: str
    name: str
    email: str
    occupation: str
    date_of_birth: str
    description: str
    created_at: str
