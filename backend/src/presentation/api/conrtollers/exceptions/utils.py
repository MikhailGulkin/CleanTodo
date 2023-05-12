from collections.abc import Awaitable, Callable
from typing import ParamSpec, Union

from blacksheep import Application, Request, Response
from src.application.common.exceptions import ApplicationException
from src.domain.common.exceptions import DomainException

asyncGeneric = Callable[[Application, Request, ApplicationException], Awaitable[Response]]
applicationErrors = type[Union[ApplicationException, DomainException]]
Param = ParamSpec("Param")


def generate_exceptions_dict(
    exceptions: list[applicationErrors], handler: asyncGeneric
) -> dict[applicationErrors, asyncGeneric]:
    result = {}
    for exc in exceptions:
        result[exc] = handler
    return result


def generate_application_handler(response: Callable[[ApplicationException], Response]) -> asyncGeneric:
    async def exception_handler(_: Application, __: Request, err: ApplicationException) -> Response:
        return response(err)

    return exception_handler
