from uuid import UUID

from blacksheep.server.controllers import get, post
from didiator import CommandMediator, QueryMediator
from src.application.user.commands import CreateUser
from src.application.user.dto import User
from src.application.user.queries import GetUserById, GetUserByUsername
from src.presentation.api.conrtollers.base_contoller import BaseAPIController
from src.presentation.api.conrtollers.decorators import setup_async_generators
from src.presentation.api.conrtollers.docs.user import user_create
from src.presentation.api.docs import docs


class UserController(BaseAPIController):
    _ENDPOINT_NAME = "users"

    @classmethod
    def class_name(cls) -> str:
        return cls._ENDPOINT_NAME

    @get("/{user_id}")
    @setup_async_generators
    async def get_user_by_id(self, user_id: UUID, mediator: QueryMediator) -> User:
        return await mediator.query(GetUserById(user_id=user_id))

    @get("/@/{username}")
    @setup_async_generators
    async def get_user_by_username(self, username: str, mediator: QueryMediator) -> User:
        return await mediator.query(GetUserByUsername(username=username))

    @post("/")
    @docs(user_create)
    @setup_async_generators
    async def create_user(self, create_user_command: CreateUser, mediator: CommandMediator) -> User:
        create_user_command.validate()
        user = await mediator.send(create_user_command)

        return user
