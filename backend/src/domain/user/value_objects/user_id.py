from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[UUID]):
    value: UUID = field(default_factory=uuid4)

    @property
    def to_uuid(self) -> UUID:
        return self.value
