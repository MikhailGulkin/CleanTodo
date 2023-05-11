from typing import cast
from uuid import UUID
from collections.abc import AsyncGenerator, Coroutine

from blacksheep import Response, text
from blacksheep.server.controllers import post, get
from didiator import CommandMediator, Mediator, QueryMediator
from blacksheep.server.responses import ok

# from src.application.user.dto import User
from src.application.user.dto import User
from src.application.user.queries import GetUserById
from src.presentation.api.conrtollers.base_contoller import BaseAPIController


class UserController(BaseAPIController):
    @get("/{user_id}")
    async def get_user_by_id(self, user_id: UUID, mediator: Coroutine[QueryMediator]) -> dict[User]:
        m: QueryMediator = await mediator
        user = await m.query(GetUserById(user_id=user_id))

        return cast(dict[User], user)
