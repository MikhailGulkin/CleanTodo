from dataclasses import dataclass

from domain.common.exceptions import DomainException


@dataclass(eq=False)
class IncorrectTaskTitle(ValueError, DomainException):
    task_title: str

    @property
    def message(self) -> str:
        return f'{self.task_title} not valid'
