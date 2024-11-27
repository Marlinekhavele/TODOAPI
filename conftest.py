import asyncio

import pytest
from httpx import AsyncClient

from app.main import app

TEST_BASE_URL = "http://test"


@pytest.fixture
def client():
    return AsyncClient(app=app)


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
