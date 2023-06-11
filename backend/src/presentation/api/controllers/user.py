from uuid import UUID

from didiator import QueryMediator
from fastapi import APIRouter, Depends, Path
from src.application.user import dto
from src.application.user.commands import CreateUser
from src.application.user.commands.create_user import BaseCreateUserHandler
from src.application.user.queries import (
    GetUserById,
    GetUserByIdHandler,
    GetUserByUsername,
)
from src.application.user.validators.username import MAX_USERNAME_LENGTH
from src.presentation.api.controllers.docs import (
    user_create,
    user_get_by_id,
    user_get_by_username,
)
from src.presentation.api.providers import Stub

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.post("/", **user_create)
async def create_user(
    create_user_command: CreateUser,
    handler: BaseCreateUserHandler = Depends(Stub(BaseCreateUserHandler)),
) -> dto.User:
    create_user_command.validate()
    print(handler)
    user = await handler(create_user_command)
    return user


@user_router.get("/{user_id}", **user_get_by_id)
async def get_user_by_id(
    user_id: UUID,
    handler: GetUserByIdHandler = Depends(Stub(GetUserByIdHandler)),
) -> dto.UserDTOs:
    user = await handler(GetUserById(user_id=user_id))
    return user


@user_router.get("/@/{username}", **user_get_by_username)
async def get_user_by_username(
    username: str = Path(max_length=MAX_USERNAME_LENGTH),
    mediator: QueryMediator = Depends(Stub(QueryMediator)),
) -> dto.User:
    user = await mediator.query(GetUserByUsername(username=username))
    return user
