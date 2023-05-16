import uuid

import pytest
import pytest_asyncio
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.models.user import User


@pytest_asyncio.fixture(scope="function")
async def create_user_in_database(db_session: AsyncSession):
    async def create_user_in_database_wrap(user_id: int, username: str, email: str, password: str):
        await db_session.execute(
            insert(User).values(
                id=user_id,
                username=username,
                email=email,
                password=password,
            )
        )
        await db_session.commit()

    return create_user_in_database_wrap


@pytest.fixture
def user_data():
    return {
        "user_id": str(uuid.uuid4()),
        "username": "string123",
        "email": "string@mail.com",
        "password": "String123",
    }
