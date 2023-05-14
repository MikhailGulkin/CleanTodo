from typing import Union

from src.application.user import dto
from src.application.user.exceptions import (
    UserEmailAlreadyExists,
    UserIdAlreadyExists,
    UserNameAlreadyExists,
)
from src.application.user.validators import (
    ToShortPassword,
    ToShortUsername,
    WrongEmailFormat,
    WrongPasswordFormat,
    WrongUsernameFormat,
)
from src.presentation.api.controllers.responses import ErrorResult
from starlette import status

user_create = {
    "responses": {
        status.HTTP_201_CREATED: {"model": dto.User},
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResult[
                Union[
                    ToShortUsername,
                    WrongUsernameFormat,
                    WrongEmailFormat,
                    ToShortPassword,
                    WrongPasswordFormat,
                ]
            ],
        },
        status.HTTP_409_CONFLICT: {
            "model": ErrorResult[
                Union[
                    UserIdAlreadyExists,
                    UserNameAlreadyExists,
                    UserEmailAlreadyExists,
                ]
            ],
        },
    },
    "status_code": status.HTTP_201_CREATED,
}
