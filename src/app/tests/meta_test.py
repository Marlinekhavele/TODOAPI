import pytest
from httpx import AsyncClient

from conftest import TEST_BASE_URL


@pytest.mark.asyncio
async def test_endpoint_meta(client: AsyncClient):
    response = await client.get(f"{TEST_BASE_URL}/api/meta/", follow_redirects=False)
    assert 200 == response.status_code
    assert {"app_version": "0.1.1"} == response.json()