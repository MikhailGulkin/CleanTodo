from dataclasses import dataclass, field
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class User(DTO):
    id: UUID
    username: str
    password: str
    email: str
    deleted: bool = field(default=False, init=False)
