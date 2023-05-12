from typing import NoReturn
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.exc import DBAPIError, IntegrityError
from src.application.common.exceptions import RepoError
from src.application.user import dto
from src.application.user.exceptions import (
    UserEmailAlreadyExists,
    UserIdAlreadyExists,
    UserIdNotExist,
    UserNameAlreadyExists,
    UserNameNotExist,
)
from src.application.user.interfaces.persistence import UserReader, UserRepo
from src.domain.common.constants import Empty
from src.domain.user import entities
from src.domain.user.value_objects import UserId
from src.infrastructure.db.exception_mapper import exception_mapper
from src.infrastructure.db.models.user import User
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class UserReaderImpl(SQLAlchemyRepo, UserReader):
    # @exception_mapper
    async def get_user_by_id(self, user_id: UUID) -> dto.UserDTOs:
        user = await self.session.scalar(
            select(User).where(
                User.id == user_id,
            )
        )
        if user is None:
            raise UserIdNotExist(user_id)

        return self._mapper.load(user, dto.UserDTOs)

    @exception_mapper
    async def get_user_by_username(self, username: str) -> dto.User:
        user = await self.session.scalar(
            select(User).where(
                User.username == username,
            )
        )
        if user is None:
            raise UserNameNotExist(username)

        return self._mapper.load(user, dto.User)

    async def get_users_count(self, deleted: bool | Empty = Empty.UNSET) -> int:
        query = select(func.count(User.id))

        if deleted is not Empty.UNSET:
            query = query.where(User.deleted == deleted)

        users_count = await self.session.scalar(query)
        return users_count or 0


class UserRepoImpl(SQLAlchemyRepo, UserRepo):
    @exception_mapper
    async def acquire_user_by_id(self, user_id: UserId) -> entities.User:
        user = await self.session.scalar(
            select(User)
            .where(
                User.id == user_id.to_uuid,
            )
            .with_for_update()
        )

        if user is None:
            raise UserIdNotExist(user_id.to_uuid)

        return self._mapper.load(user, entities.User)

    @exception_mapper
    async def add_user(self, user: entities.User) -> None:
        db_user = self._mapper.load(user, User)
        self.session.add(db_user)
        try:
            await self.session.flush((db_user,))
        except IntegrityError as err:
            self._parse_error(err, user)

    def _parse_error(self, err: DBAPIError, user: entities.User) -> NoReturn:
        match err.__cause__.__cause__.constraint_name:  # type: ignore
            case "pk_users":
                raise UserIdAlreadyExists(user.id.to_uuid) from err
            case "uq_users_username":
                raise UserNameAlreadyExists(str(user.username)) from err
            case "uq_users_email":
                raise UserEmailAlreadyExists(str(user.email)) from err
            case _:
                raise RepoError from err
