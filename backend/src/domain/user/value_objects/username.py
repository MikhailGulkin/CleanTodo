from dataclasses import dataclass

from src.domain.user.exceptions import IncorrectUserName
from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserName(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise IncorrectUserName(username=self.value)
