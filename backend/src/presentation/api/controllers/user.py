from didiator import CommandMediator
from fastapi import APIRouter, Depends
from src.application.user import dto
from src.application.user.commands import CreateUser
from src.presentation.api.controllers.docs import user_create
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
    user = await mediator.send(create_user_command)
    return user
