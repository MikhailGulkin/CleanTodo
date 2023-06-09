from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from sqlalchemy.exc import SQLAlchemyError
from src.application.common.exceptions import RepoError

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
Func = Callable[Param, Coroutine[Any, Any, ReturnType]]  # type: ignore[valid-type]


def exception_mapper(func: Func) -> Func:
    @wraps(func)  # type: ignore[arg-type]
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise RepoError from err

    return wrapped
