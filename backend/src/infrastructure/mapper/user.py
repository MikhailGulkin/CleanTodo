from typing import cast

from adaptix.load_error import ValueLoadError
from src.application.user import dto
from src.domain.user import entities
from src.domain.user import value_objects as vo
from src.infrastructure.db import models


def convert_user_entity_to_dto(user: entities.User) -> dto.User:
    if user.deleted:
        raise ValueLoadError(f"User {user} is deleted")

    return dto.User(
        id=user.id.to_uuid,
        username=str(user.username),
        password=str(user.password),
        email=str(user.email),
    )


def convert_user_entity_to_db_model(user: entities.User) -> models.User:
    return models.User(
        id=user.id.to_uuid,
        username=str(user.username),
        password=str(user.password),
        email=str(user.email),
        deleted=user.deleted,
    )


def convert_db_model_to_user_entity(user: models.User) -> entities.User:
    return entities.User(
        id=vo.UserId(user.id),
        username=vo.UserName(user.username),
        password=vo.UserPassword(user.password),
        email=vo.UserEmail(user.email),
        deleted=user.deleted,
    )


def convert_db_model_to_user_dto(user: models.User) -> dto.User:
    if user.deleted:
        raise ValueLoadError(f"User {user} is deleted")

    return dto.User(
        id=user.id,
        username=cast(str, user.username),
        password=cast(str, user.password),
        email=cast(str, user.email),
    )
