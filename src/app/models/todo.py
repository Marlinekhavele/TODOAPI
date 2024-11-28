from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.base import Base
from app.schemas.enums.todo import TodoStatus


class Todo(Base):
    __tablename__ = "todos"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="todo_pk"),
        UniqueConstraint(
            "id",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    description = sa.Column(sa.String(200))
    status = sa.Column(sa.Enum(TodoStatus))
    created_at = sa.Column(sa.DateTime, server_default=func.now(), nullable=False)
    updated_at = sa.Column(
        sa.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
