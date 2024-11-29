import uuid
from datetime import datetime

from pydantic import BaseModel

from app.schemas.enums.todo import TodoStatus


class TodoSchema(BaseModel):
    title: str
    description: str
    status: TodoStatus

    model_config = {"use_enum_values": True}


class TodoResponse(TodoSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"form_attributes": True, "use_enum_values": True}
