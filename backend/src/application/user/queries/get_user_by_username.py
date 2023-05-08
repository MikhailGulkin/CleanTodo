import logging
from dataclasses import dataclass

from src.application.common.query import Query, QueryHandler
from src.application.user import dto, validators
from src.application.user.interfaces import UserReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class GetUserByUsername(Query[dto.User]):
    username: str

    def __post_init__(self) -> None:
        validators.validate_username(self.username)


class GetUserByUsernameHandler(QueryHandler[GetUserByUsername, dto.User]):
    def __init__(self, user_reader: UserReader) -> None:
        self._user_reader = user_reader

    async def __call__(self, query: GetUserByUsername) -> dto.User:
        user = await self._user_reader.get_user_by_username(query.username)
        # logger.debug("Get use by username", extra={"username": query.username, "user": user})
        return user
