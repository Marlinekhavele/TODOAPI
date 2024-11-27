
from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(
    title="todo-app-api",
)


app.include_router(api_router, prefix="/api")