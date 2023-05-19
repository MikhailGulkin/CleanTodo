import pytest
from httpx import AsyncClient
from starlette import status


@pytest.mark.asyncio
async def test_get_user_by_username(client: AsyncClient, create_user_in_database, correct_user_data) -> None:
    await create_user_in_database(**correct_user_data)
    key = "username"

    response = await client.get(f"/users/@/{correct_user_data.get(key)}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get(key) == correct_user_data.get(key)


@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient, create_user_in_database, correct_user_data) -> None:
    await create_user_in_database(**correct_user_data)
    key = "user_id"
    response_key = "id"

    response = await client.get(f"/users/{correct_user_data.get(key)}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get(response_key) == correct_user_data.get(key)


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, correct_user_data) -> None:
    key = "username"
    response = await client.post("/users/", json=correct_user_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()[key] == correct_user_data[key]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ["invalid_user_data", "status_code"],
    [
        (pytest.lazy_fixture("to_short_username_user_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
        (pytest.lazy_fixture("wrong_username_format_user_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
        (pytest.lazy_fixture("wrong_email_format_username_user_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
        (pytest.lazy_fixture("to_short_password_user_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
        (pytest.lazy_fixture("wrong_password_format_user_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
    ],
)
async def test_invalid_create_user(client: AsyncClient, invalid_user_data, status_code) -> None:
    response = await client.post("/users/", json=invalid_user_data)

    assert response.status_code == status_code


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "invalid_user_data, status_code",
    [
        (pytest.lazy_fixture("correct_user_data"), status.HTTP_409_CONFLICT),
        (pytest.lazy_fixture("username_already_exist_user_data"), status.HTTP_409_CONFLICT),
        (pytest.lazy_fixture("email_already_exist_user_data"), status.HTTP_409_CONFLICT),
    ],
)
async def test_conflict_create_user(
    client: AsyncClient, create_user_in_database, correct_user_data, invalid_user_data, status_code
) -> None:
    await create_user_in_database(**correct_user_data)
    response = await client.post("/users/", json=invalid_user_data)

    assert response.status_code == status_code
