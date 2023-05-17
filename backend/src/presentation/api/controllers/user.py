from uuid import UUID

from didiator import CommandMediator, QueryMediator
from fastapi import APIRouter, Depends, Path
from src.application.user import dto
from src.application.user.commands import CreateUser
from src.application.user.queries import GetUserById, GetUserByUsername
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
    mediator: CommandMediator = Depends(Stub(CommandMediator)),
) -> dto.User:
    create_user_command.validate()

    user = await mediator.send(create_user_command)
    return user


@user_router.get("/{user_id}", **user_get_by_id)
async def get_user_by_id(
    user_id: UUID,
    mediator: QueryMediator = Depends(Stub(QueryMediator)),
) -> dto.UserDTOs:
    user = await mediator.query(GetUserById(user_id=user_id))
    return user


@user_router.get("/@/{username}", **user_get_by_username)
async def get_user_by_username(
    username: str = Path(max_length=MAX_USERNAME_LENGTH),
    mediator: QueryMediator = Depends(Stub(QueryMediator)),
) -> dto.User:
    user = await mediator.query(GetUserByUsername(username=username))
    return user
