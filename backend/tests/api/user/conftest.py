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
def correct_user_data():
    return {
        "user_id": str(uuid.uuid4()),
        "username": "string123",
        "email": "string@mail.com",
        "password": "String123",
    }


@pytest.fixture
def to_short_username_user_data(correct_user_data):
    correct_user_data["username"] = "1"  # To short
    return correct_user_data


@pytest.fixture
def wrong_username_format_user_data(correct_user_data):
    correct_user_data["username"] = "9" * 9  # Invalid format
    return correct_user_data


@pytest.fixture
def wrong_email_format_username_user_data(correct_user_data):
    correct_user_data["email"] = "mail"  # Invalid format
    return correct_user_data


@pytest.fixture
def to_short_password_user_data(correct_user_data):
    correct_user_data["password"] = "1"  # To short
    return correct_user_data


@pytest.fixture
def wrong_password_format_user_data(correct_user_data):
    correct_user_data["password"] = "mail"  # Invalid format
    return correct_user_data


@pytest.fixture
def username_already_exist_user_data(correct_user_data):
    correct_user_data["user_id"] = str(uuid.uuid4())
    return correct_user_data


@pytest.fixture
def email_already_exist_user_data(correct_user_data):
    correct_user_data["user_id"] = str(uuid.uuid4())
    correct_user_data["username"] = f'T{correct_user_data["username"]}'
    return correct_user_data
