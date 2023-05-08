from dataclasses import dataclass

from src.domain.common.value_objects.base import ValueObject
from src.domain.task.constants import Status


@dataclass(frozen=True)
class TaskStatus(ValueObject[Status]):
    value: Status
