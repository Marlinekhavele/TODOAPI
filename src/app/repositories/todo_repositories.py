import uuid
from datetime import datetime

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models.todo import Todo
from app.schemas.enums.todo import TodoStatus
from app.schemas.todo_schema import TodoResponse


class TodoRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_todo(self, todo_data) -> TodoResponse:
        # Create a new Todo object
        new_todo = Todo(
            title=todo_data.title,
            description=todo_data.description,
            status=TodoStatus(todo_data.status),
        )
        self.db.add(new_todo)
        await self.db.commit()
        await self.db.refresh(new_todo)
        return TodoResponse(
            id=new_todo.id,
            title=todo_data.title,
            description=new_todo.description,
            status=new_todo.status,
            created_at=new_todo.created_at,
            updated_at=new_todo.updated_at,
        )

    async def get_todos(self) -> list[TodoResponse]:
        results = await self.db.execute(select(Todo))
        todos = results.scalars().all()
        return [
            TodoResponse(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                status=todo.status,
                created_at=todo.created_at,
                updated_at=todo.updated_at,
            )
            for todo in todos
        ]

    async def get_todo_by_id(self, todo_id: uuid.UUID) -> Todo:
        query = select(Todo).filter(Todo.id == todo_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def update_todo(
        self, todo_id: uuid.UUID, title: str, description: str, status: TodoStatus
    ) -> TodoResponse:
        todo_obj = await self.get_todo_by_id(todo_id)
        if todo_obj:
            todo_obj.title = title
            todo_obj.description = description
            todo_obj.status = status
            todo_obj.updated_at = datetime.utcnow()  # Manually update the timestamp
            await self.db.commit()
            await self.db.refresh(todo_obj)  # Refresh to get the updated data
            return TodoResponse(
                id=todo_obj.id,
                title=todo_obj.title,
                description=todo_obj.description,
                status=todo_obj.status,
                created_at=todo_obj.created_at,
                updated_at=todo_obj.updated_at,
            )
        return None

    async def delete_todo(self, todo_id: uuid.UUID):
        query = select(Todo).filter(Todo.id == todo_id)
        result = await self.db.execute(query)
        todo_obj = result.scalar_one_or_none()
        if todo_obj:
            await self.db.delete(todo_obj)
            await self.db.commit()
            return TodoResponse(
                id=todo_obj.id,
                title=todo_obj.title,
                description=todo_obj.description,
                status=todo_obj.status,
                created_at=todo_obj.created_at,
                updated_at=todo_obj.updated_at,
            )
        return None
