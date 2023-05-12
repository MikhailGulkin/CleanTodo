import dataclasses
from datetime import datetime, timedelta

from src.domain.common.constants import Empty
from src.domain.common.entities import Entity
from src.domain.task.constants import Status
from src.domain.task.value_objects.task_id import TaskId
from src.domain.task.value_objects.task_priority import TaskPriority
from src.domain.task.value_objects.task_status import TaskStatus


@dataclasses.dataclass
class Task(Entity):
    id: TaskId
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    deadline: datetime
    updated_at: datetime = dataclasses.field(default_factory=datetime.now)
    created_at: datetime = dataclasses.field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        task_id: TaskId,
        title: str,
        description: str,
        status: TaskStatus = TaskStatus(value=Status.IN_PROCESS),
        priority: TaskPriority = TaskPriority(value=1),
        deadline: datetime = datetime.now() + timedelta(days=1),
    ) -> "Task":
        return Task(
            id=task_id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            deadline=deadline,
        )

    def update(
        self,
        title: str | Empty = Empty.UNSET,
        description: str | Empty = Empty.UNSET,
        status: TaskStatus | Empty = Empty.UNSET,
        priority: TaskPriority | Empty = Empty.UNSET,
        deadline: datetime | Empty = Empty.UNSET,
    ) -> None:
        self.updated_at = datetime.now()

        if title is not Empty.UNSET:
            self.title = title
        if description is not Empty.UNSET:
            self.description = description
        if status is not Empty.UNSET:
            self.status = status
        if priority is not Empty.UNSET:
            self.priority = priority
        if deadline is not Empty.UNSET:
            self.deadline = deadline
