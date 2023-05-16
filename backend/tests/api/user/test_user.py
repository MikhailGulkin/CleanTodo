import pytest
from httpx import AsyncClient
from starlette import status


@pytest.mark.asyncio
async def test_get_user_by_username(client: AsyncClient, create_user_in_database, user_data) -> None:
    await create_user_in_database(**user_data)
    key = "username"

    response = await client.get(f"/users/@/{user_data.get(key)}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get(key) == user_data.get(key)


@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient, create_user_in_database, user_data) -> None:
    await create_user_in_database(**user_data)
    key = "user_id"
    response_key = "id"

    response = await client.get(f"/users/{user_data.get(key)}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get(response_key) == user_data.get(key)


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, user_data) -> None:
    key = "username"
    response = await client.post("/users/", json=user_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()[key] == user_data[key]
