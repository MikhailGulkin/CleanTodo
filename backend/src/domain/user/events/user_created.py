import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event


@dataclasses.dataclass(frozen=True)
class UserCreated(Event):  # noqa
    id: UUID
    username: str
    password: str
    email: str
