from datetime import datetime
from pydantic import BaseModel

class PostInput(BaseModel):
    id: int | None = None
    title: str
    content: str

class PostOutput(BaseModel):
    id: int | None
    title: str
    content: str
    created_at: datetime
    updated_at: datetime | None

    #class ConfigDict:
    #    from_attributes = True
