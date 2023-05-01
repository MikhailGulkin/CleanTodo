import re
from dataclasses import dataclass

from src.domain.user.value_objects.consts import PASSWORD_REGEX
from src.domain.user.exceptions import IncorrectPassword
from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserPassword(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if len(self.value) < 8:
            raise IncorrectPassword(
                password=self.value,
                additional_text="Password length must be more than 7 characters"
            )
        if not re.fullmatch(PASSWORD_REGEX, self.value):
            raise IncorrectPassword(
                password=self.value
            )
