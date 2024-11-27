from fastapi import APIRouter

from app.api import health, meta, todo

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(todo.router, tags=["Todo"])
api_router.include_router(meta.router, tags=["meta"])
