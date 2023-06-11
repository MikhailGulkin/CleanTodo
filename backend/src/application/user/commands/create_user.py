import abc
from abc import ABC
from dataclasses import dataclass

from src.application.common.command import Command
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.user import dto, validators
from src.application.user.interfaces import UserRepo
from src.domain.user.entities import User
from src.domain.user.value_objects import UserEmail, UserName, UserPassword


@dataclass(frozen=True)
class CreateUser(Command[dto.User]):
    username: str
    password: str
    email: str

    def validate(self) -> None:
        validators.validate_username(self.username)
        validators.validate_email(self.email)
        validators.validate_password(self.password)


class BaseCreateUserHandler(ABC):
    @abc.abstractmethod
    def __init__(self, user_repo: UserRepo, uow: UnitOfWork, mapper: Mapper) -> None:
        self._user_repo = user_repo
        self._uow = uow
        self._mapper = mapper

    @abc.abstractmethod
    async def __call__(self, command: CreateUser) -> dto.User:
        pass


class CreateUserHandler(BaseCreateUserHandler):
    def __init__(self, user_repo: UserRepo, uow: UnitOfWork, mapper: Mapper) -> None:
        super().__init__(user_repo, uow, mapper)

    async def __call__(self, command: CreateUser) -> dto.User:
        user = User.create(
            username=UserName(command.username),
            email=UserEmail(command.email),
            password=UserPassword(command.password),
        )

        await self._user_repo.add_user(user)
        # await self._mediator.publish(user.pull_events())
        await self._uow.commit()

        user_dto = self._mapper.load(user, dto.User)
        return user_dto
