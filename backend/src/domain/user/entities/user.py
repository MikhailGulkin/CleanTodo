import dataclasses
import datetime

from domain.common.entities import Entity
from domain.user.value_objects import (
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
    created_at: datetime.datetime = dataclasses.field(
        default_factory=datetime.datetime.now
    )
