from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC):
    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        """This method checks that a value is valid to create this value object"""
        pass


@dataclass(frozen=True)
class ValueObject(BaseValueObject, Generic[T]):
    value: T

    def __str__(self) -> str:
        return str(self.value)

    def __int__(self) -> int:
        return int(self.value)
