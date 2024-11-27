from pydantic import BaseModel


class TodoSchema(BaseModel):
    description: str
    status: str
