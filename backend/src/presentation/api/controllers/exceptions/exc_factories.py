from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeAlias, Union

from fastapi.responses import ORJSONResponse
from src.application.common.exceptions import ApplicationException
from src.domain.common.exceptions import DomainException
from starlette.requests import Request

Response: TypeAlias = ORJSONResponse
applicationErrors = type[Union[ApplicationException, DomainException]]
asyncGeneric = Callable[[Request, applicationErrors], Awaitable[Response]]

Param = ParamSpec("Param")


def generate_exceptions_dict(
    exceptions: list[applicationErrors], handler: asyncGeneric
) -> dict[applicationErrors, asyncGeneric]:
    result = {}
    for exc in exceptions:
        result[exc] = handler
    return result


def generate_application_handler(response: Callable[[applicationErrors], Response]) -> asyncGeneric:
    async def exception_handler(_: Request, err: applicationErrors) -> Response:
        return response(err)

    return exception_handler
