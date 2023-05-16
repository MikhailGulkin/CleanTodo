import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_something(client: AsyncClient, create_user_in_database, user_data) -> None:
    await create_user_in_database(**user_data)

    response = await client.get("/users/@/string")
    print(response.json())
