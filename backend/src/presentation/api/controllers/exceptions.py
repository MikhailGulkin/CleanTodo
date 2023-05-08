import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status
from starlette.requests import Request

from src.application.user.exceptions import UserIdAlreadyExists, UserIdNotExist, UserNameAlreadyExists, UserNameNotExist
from src.application.user.validators.username import ToShortUsername, WrongUsernameFormat
from src.domain.user.exceptions import UserIsDeleted
from src.presentation.api.controllers.responses import ErrorResult

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)


async def exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    logger.error("Handle error", exc_info=err, extra={"error": err})

    match err:
        case ToShortUsername() | WrongUsernameFormat() as err:
            return ORJSONResponse(ErrorResult(message=err.message, data=err), status_code=status.HTTP_400_BAD_REQUEST)
        case UserIdNotExist() | UserNameNotExist() as err:
            return ORJSONResponse(ErrorResult(message=err.message, data=err), status_code=status.HTTP_404_NOT_FOUND)
        case UserNameAlreadyExists() | UserIdAlreadyExists() | UserIsDeleted() as err:
            return ORJSONResponse(ErrorResult(message=err.message, data=err), status_code=status.HTTP_409_CONFLICT)
        case _:
            logger.exception("Unknown error occurred", exc_info=err, extra={"error": err})
            return ORJSONResponse(
                ErrorResult(message="Unknown server error has occurred", data=err),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
