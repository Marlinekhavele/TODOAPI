from pydantic import BaseModel

from app.schemas.enums.todo import TodoStatus


class TodoSchema(BaseModel):
    description: str
    status: TodoStatus

    class Config:
        use_enum_values = True
