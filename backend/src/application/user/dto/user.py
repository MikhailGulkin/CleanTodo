from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from uuid import UUID

from src.application.common.dto import DTO


@dataclass(frozen=True)
class User(DTO):
    id: UUID
    username: str
    password: str
    email: str
    deleted: Literal[False] = field(default=False, init=False)
