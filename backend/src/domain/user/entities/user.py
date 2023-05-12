import dataclasses
from dataclasses import dataclass
from typing import Literal

from src.domain.common.constants import Empty
from src.domain.common.entities import AggregateRoot
from src.domain.user.events import UserCreated
from src.domain.user.value_objects import UserEmail, UserId, UserName, UserPassword


@dataclass
class User(AggregateRoot):
    id: UserId
    username: UserName
    password: UserPassword
    email: UserEmail
    deleted: Literal[False] = dataclasses.field(default=False, kw_only=True)

    @classmethod
    def create(
        cls,
        user_id: UserId,
        username: UserName,
        password: UserPassword,
        email: UserEmail,
    ) -> "User":
        user = User(id=user_id, username=username, password=password, email=email)
        user.record_event(
            UserCreated(
                id=user_id.to_uuid,
                username=str(username),
                password=str(password),
                email=str(email),
            )
        )
        return user

    def update(
        self,
        username: UserName | Empty = Empty.UNSET,
        email: UserEmail | Empty = Empty.UNSET,
        password: UserPassword | Empty = Empty.UNSET,
    ) -> None:
        if username is not Empty.UNSET:
            self.username = username
        if email is not Empty.UNSET:
            self.email = email
        if password is not Empty.UNSET:
            self.password = password
