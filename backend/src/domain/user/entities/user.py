import dataclasses
import datetime

from src.domain.common.constants import Empty
from src.domain.common.entities import Entity

from src.domain.user.value_objects import (
    UserEmail,
    UserName,
    UserId,
    UserPassword
)


@dataclasses.dataclass
class User(Entity):
    id: UserId
    username: UserName
    password: UserPassword
    email: UserEmail
    deleted: bool = dataclasses.field(default=False, kw_only=True)
    created_at: datetime.datetime = dataclasses.field(
        default_factory=datetime.datetime.now
    )

    @classmethod
    def create(cls, user_id: UserId, username: UserName, password: UserPassword, email: UserEmail) -> 'User':
        return User(id=user_id, username=username, password=password, email=email)

    def update(
            self,
            username: UserName | Empty = Empty.UNSET,
            email: UserEmail | Empty = Empty.UNSET,
            password: UserPassword | Empty = Empty.UNSET
    ) -> None:

        if username is not Empty.UNSET:
            self.username = username
        if email is not Empty.UNSET:
            self.email = email
        if password is not Empty.UNSET:
            self.password = password
