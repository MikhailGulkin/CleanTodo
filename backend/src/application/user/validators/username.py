import re
from dataclasses import dataclass

from src.application.common.validators import ValidatorError

MIN_USERNAME_LENGTH = 2
MAX_USERNAME_LENGTH = 32
USERNAME_PATTERN = re.compile(r"[A-Za-z][A-Za-z1-9_]+")


@dataclass(eq=False)
class WrongUsernameValue(ValueError, ValidatorError):
    username: str


class ToShortUsername(WrongUsernameValue):
    pass


class WrongUsernameFormat(WrongUsernameValue):
    pass


def validate_username(username: str) -> None:
    if not(MIN_USERNAME_LENGTH < len(username) < MAX_USERNAME_LENGTH):
        raise ToShortUsername(username)

    if not USERNAME_PATTERN.match(username):
        raise WrongUsernameFormat(username)
