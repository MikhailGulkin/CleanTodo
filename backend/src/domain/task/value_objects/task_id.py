from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class TaskId(ValueObject[int]):
    value: int
