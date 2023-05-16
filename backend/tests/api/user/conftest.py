import uuid

import pytest
import pytest_asyncio
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from src.infrastructure.db.models.user import User


@pytest_asyncio.fixture(scope="function")
async def create_user_in_database(db_session_test: async_sessionmaker[AsyncSession]):
    async def create_user_in_database_wrap(user_id: int, username: str, email: str, password: str):
        async with db_session_test() as session:
            await session.execute(
                insert(User).values(
                    id=user_id,
                    username=username,
                    email=email,
                    password=password,
                )
            )
            await session.commit()

    return create_user_in_database_wrap


@pytest.fixture
def user_data():
    return {
        "user_id": uuid.uuid4(),
        "username": "string",
        "email": "string",
        "password": "string",
    }
