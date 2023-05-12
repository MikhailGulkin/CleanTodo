#
from http import HTTPStatus

from blacksheep import Application, json
from src.application.user.exceptions import (
    UserEmailAlreadyExists,
    UserIdAlreadyExists,
    UserIdNotExist,
    UserNameAlreadyExists,
    UserNameNotExist,
)
from src.application.user.validators import (
    ToShortPassword,
    ToShortUsername,
    WrongEmailFormat,
    WrongPasswordFormat,
    WrongUsernameFormat,
)
from src.domain.user.exceptions import UserIsDeleted
from src.presentation.api.conrtollers.exceptions.utils import (
    applicationErrors,
    asyncGeneric,
    generate_application_handler,
    generate_exceptions_dict,
)
from src.presentation.api.conrtollers.responses import ErrorResult


def setup_exception_handlers(app: Application) -> None:
    app.exceptions_handlers.update(
        {
            **user_not_exist_handlers(),
            **user_invalid_params_create_handlers(),
            **user_conflict_create_handlers(),
        }
    )


def user_not_exist_handlers() -> dict[applicationErrors, asyncGeneric]:
    return generate_exceptions_dict(
        [UserIdNotExist, UserNameNotExist],
        generate_application_handler(
            lambda err: json(
                ErrorResult(message=err.message, data=err).dict(),
                status=HTTPStatus.NOT_FOUND,
            )
        ),
    )


def user_invalid_params_create_handlers() -> dict[applicationErrors, asyncGeneric]:
    return generate_exceptions_dict(
        [
            ToShortUsername,
            WrongUsernameFormat,
            WrongEmailFormat,
            ToShortPassword,
            WrongPasswordFormat,
        ],
        generate_application_handler(
            lambda err: json(
                ErrorResult(message=err.message, data=err).dict(),
                status=HTTPStatus.BAD_REQUEST,
            )
        ),
    )


def user_conflict_create_handlers() -> dict[applicationErrors, asyncGeneric]:
    return generate_exceptions_dict(
        [
            UserIdAlreadyExists,
            UserNameAlreadyExists,
            UserIsDeleted,
            UserEmailAlreadyExists,
        ],
        generate_application_handler(
            lambda err: json(
                ErrorResult(message=err.message, data=err).dict(),
                status=HTTPStatus.CONFLICT,
            )
        ),
    )
