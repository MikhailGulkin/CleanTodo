from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
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
from src.presentation.api.controllers.exceptions.exc_factories import (
    applicationErrors,
    asyncGeneric,
    generate_application_handler,
    generate_exceptions_dict,
)
from src.presentation.api.controllers.responses import ErrorResult
from starlette import status


def setup_exception_handlers(app: FastAPI) -> None:
    for exception, handler in {
        **user_not_exist_handlers(),
        **user_conflict_create_handlers(),
        **user_invalid_params_create_handlers(),
    }.items():
        app.add_exception_handler(exception, handler)


def user_not_exist_handlers() -> dict[applicationErrors, asyncGeneric]:
    return generate_exceptions_dict(
        [UserIdNotExist, UserNameNotExist],
        generate_application_handler(
            lambda err: ORJSONResponse(
                ErrorResult(err.message, err).dict(),
                status_code=status.HTTP_404_NOT_FOUND,
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
            lambda err: ORJSONResponse(
                ErrorResult(err.message, err).dict(),
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        ),
    )


def user_conflict_create_handlers() -> dict[applicationErrors, asyncGeneric]:
    return generate_exceptions_dict(
        [
            UserIdAlreadyExists,
            UserNameAlreadyExists,
            UserEmailAlreadyExists,
        ],
        generate_application_handler(
            lambda err: ORJSONResponse(
                ErrorResult(err.message, err).dict(),
                status_code=status.HTTP_409_CONFLICT,
            )
        ),
    )
