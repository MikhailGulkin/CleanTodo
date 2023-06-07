import dataclasses
from uuid import UUID

from didiator import CommandMediator, QueryMediator
from fastapi import Depends, Path
from sanic import Blueprint, Request, json
from sanic.response import JSONResponse
from sanic_ext.extensions.openapi import openapi
from sanic_ext.extensions.openapi.definitions import RequestBody
from src.application.user import dto
from src.application.user.commands import CreateUser
from src.application.user.queries import GetUserById, GetUserByUsername
from src.application.user.validators.username import MAX_USERNAME_LENGTH
from src.presentation.api.providers import Stub

user_router = Blueprint(
    name="user_router",
    url_prefix="/users",
)


@user_router.post("/")
@openapi.definition(
    body=RequestBody(CreateUser, required=True),
)
async def create_user(
    request: Request,
    mediator: CommandMediator,
) -> JSONResponse:
    command = CreateUser(
        username=request.json.get("username"),
        password=request.json.get("password"),
        email=request.json.get("email"),
    )
    # command.validate()

    user = await mediator.send(command)
    d = dataclasses.asdict(user)
    d["id"] = str(user.id)
    return json(body=d)


@user_router.get("/<user_id>")
async def get_user_by_id(_: Request, user_id: UUID, mediator: QueryMediator) -> JSONResponse:
    user = await mediator.query(GetUserById(user_id=user_id))
    d = dataclasses.asdict(user)
    d["id"] = str(user.id)
    return json(body=d)


@user_router.get("/@/{username}")
async def get_user_by_username(
    username: str = Path(max_length=MAX_USERNAME_LENGTH),
    mediator: QueryMediator = Depends(Stub(QueryMediator)),
) -> dto.User:
    user = await mediator.query(GetUserByUsername(username=username))
    return user
