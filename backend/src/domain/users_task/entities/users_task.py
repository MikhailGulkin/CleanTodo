import dataclasses
from dataclasses import field

from src.domain.common.entities import Entity
from src.domain.task.entities.task import Task
from src.domain.task.value_objects.task_id import TaskId

from src.domain.user.value_objects import (
    UserId,
)
from src.domain.users_task.exceptions import AlreadyCreateTask, AlreadyTitleExist


@dataclasses.dataclass
class UsersTask(Entity):
    user_id: UserId
    tasks: list[Task] = field(default_factory=list)

    @classmethod
    def create(cls, user_id: UserId) -> 'UsersTask':
        return UsersTask(user_id=user_id)

    def append_users_task(
            self,
            task_id: TaskId,
            title: str,
            **kwargs
    ) -> None:
        self._user_already_create_task(task_id, title)
        self.tasks.append(Task(id=task_id, title=title, **kwargs))

    def _user_already_create_task(self, task_id: TaskId, title: str):
        for task in self.tasks:
            if task.id == task_id:
                raise AlreadyCreateTask(user_id=self.user_id, task_id=task_id)
            if task.title == title:
                AlreadyTitleExist(title=title, user_id=self.user_id, task_id=task_id)
