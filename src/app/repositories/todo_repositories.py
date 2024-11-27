import uuid
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from app.deps import get_db_session
from app.models.todo import Todo

class TodoRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_todo(self, todo_data):
        new_todo = Todo(
            description=todo_data.description,
            status=todo_data.status,
        )
        self.db.add(new_todo)
        await self.db.commit()
        await self.db.refresh(new_todo)
        return new_todo

    async def get_todos(self):
        results = await self.db.execute(select(Todo))
        todos = results.scalars().all()
        return todos

    async def get_todo_by_id(self, todo_id: uuid.UUID):
        try:
            query = select(Todo).filter(Todo.id == todo_id)
            result = await self.db.execute(query)
            todo_obj = result.scalar_one()
            return todo_obj
        except NoResultFound:
            return None

    async def update_todo(
        self, todo_id: uuid.UUID, description: str, status: str
    ):
        todo_obj = await self.get_todo_by_id(todo_id)
        if todo_obj:
            todo_obj.description = description
            todo_obj.status = status
            await self.db.commit()
        return todo_obj

    async def delete_todo(self, todo_id: uuid.UUID):
        todo_obj = await self.get_todo_by_id(todo_id)
        if todo_obj:
            self.db.delete(todo_obj)
            await self.db.commit()