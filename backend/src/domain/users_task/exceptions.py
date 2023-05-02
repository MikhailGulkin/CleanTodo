from dataclasses import dataclass

from src.domain.common.exceptions import DomainException
from src.domain.task.value_objects.task_id import TaskId
from src.domain.user.value_objects import UserId


@dataclass(eq=False)
class AlreadyCreateTask(RuntimeError, DomainException):
    task_id: TaskId
    user_id: UserId

    @property
    def message(self) -> str:
        return f"User \"{self.user_id}\" has already create " \
               f"task \"{self.task_id}"


@dataclass
class AlreadyTitleExist(RuntimeError, DomainException):
    title: str
    task_id: TaskId
    user_id: UserId

    @property
    def message(self) -> str:
        return f"Task with title: {self.title} already exist, and created:" \
               f"User: {self.user_id}"
