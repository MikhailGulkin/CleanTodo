from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.application.user.exceptions import UserIdAlreadyExists, UserNameAlreadyExists
from src.application.user.validators import (
    ToShortPassword,
    ToShortUsername,
    WrongEmailFormat,
    WrongPasswordFormat,
    WrongUsernameFormat,
)
from src.domain.user.exceptions import UserIsDeleted
from src.presentation.api.controllers.responses import ErrorResult
from starlette import status
from starlette.requests import Request


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)


async def exception_handler(_: Request, err: Exception) -> ORJSONResponse:
    match err:
        case ToShortUsername() | WrongUsernameFormat() | WrongEmailFormat() | ToShortPassword() | WrongPasswordFormat() as err:  # noqa line excp
            return ORJSONResponse(ErrorResult(message=err.message, data=err), status_code=status.HTTP_400_BAD_REQUEST)
        case UserNameAlreadyExists() | UserIdAlreadyExists() | UserIsDeleted() as err:
            return ORJSONResponse(ErrorResult(message=err.message, data=err), status_code=status.HTTP_409_CONFLICT)
        case _:
            return ORJSONResponse(
                ErrorResult(message="Unknown server error has occurred", data=err),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
