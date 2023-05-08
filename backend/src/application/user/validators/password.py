import re
from dataclasses import dataclass

from src.application.common.validators import ValidatorError

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 32
PASSWORD_PATTERN = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d].+$')


@dataclass(eq=False)
class WrongPasswordValue(ValueError, ValidatorError):
    password: str


class ToShortPassword(WrongPasswordValue):
    pass


class WrongPasswordFormat(WrongPasswordValue):
    pass


def validate_password(password: str) -> None:
    if not(MIN_PASSWORD_LENGTH < len(password) < MAX_PASSWORD_LENGTH):
        raise ToShortPassword(password)

    if not PASSWORD_PATTERN.match(password):
        raise WrongPasswordFormat(password)
