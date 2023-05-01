import re
from dataclasses import dataclass

from src.domain.user.value_objects.constants import EMAIL_REGEX
from src.domain.user.exceptions import IncorrectUserEmail
from src.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserEmail(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not re.fullmatch(EMAIL_REGEX, self.value):
            raise IncorrectUserEmail(user_email=self.value)
