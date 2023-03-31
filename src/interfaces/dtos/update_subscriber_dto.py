from typing import Optional
from pydantic import BaseModel


class UpdateSubscriberDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None
    date_of_birth: Optional[str] = None
    description: Optional[str] = None
