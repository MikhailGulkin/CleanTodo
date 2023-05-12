from dataclasses import dataclass

from src.domain.common.constants import Empty

from .user import User

UserDTOs = User


@dataclass(frozen=True)
class Users:
    users: list[UserDTOs]
    total: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
