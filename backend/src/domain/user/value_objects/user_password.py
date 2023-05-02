from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserPassword(ValueObject[str]):
    value: str
