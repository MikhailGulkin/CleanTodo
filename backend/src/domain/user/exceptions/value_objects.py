from dataclasses import dataclass
from src.domain.common.exceptions import DomainException


@dataclass(eq=False)
class IncorrectUserEmail(ValueError, DomainException):
    user_email: str

    @property
    def message(self) -> str:
        return f'{self.user_email} not valid'


@dataclass(eq=False)
class IncorrectUserName(ValueError, DomainException):
    username: str

    @property
    def message(self) -> str:
        return f'{self.username} not valid'


@dataclass(eq=False)
class IncorrectPassword(ValueError, DomainException):
    password: str
    additional_text: str = ''

    def __post_init__(self):
        self.additional_text = f'\n{self.additional_text}' if self.additional_text else ''

    @property
    def message(self) -> str:
        return f'{self.password} not valid' \
               f'{self.additional_text}'
