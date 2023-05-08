from enum import Enum


class Status(Enum):
    IN_PROCESS = "Task in process"
    COMPLETED = 'Task completed'
    CANCELED = 'Task canceled'
