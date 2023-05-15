import re
from dataclasses import dataclass

from src.application.common.validators import ValidatorError

EMAIL_PATTERN = re.compile(r"([A-Za-z0-9]+)[.-_]?([A-Za-z0-9]+)@([A-Za-z0-9-]+)(\.[A-Z|a-z]{2,})+")


@dataclass(eq=True)
class WrongEmailValue(ValueError, ValidatorError):
    email: str


@dataclass(eq=False)
class WrongEmailFormat(WrongEmailValue):
    pass


def validate_email(password: str) -> None:
    if not EMAIL_PATTERN.match(password):
        raise WrongEmailFormat(password)
