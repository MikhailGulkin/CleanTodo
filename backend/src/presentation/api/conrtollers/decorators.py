import inspect
from functools import wraps

from blacksheep import Response
from blacksheep.server.normalization import ensure_response


def setup_async_generators(next_handler):
    @wraps(next_handler)
    async def wrapped(*args, **kwargs) -> Response:
        new_args = []
        for arg in args:
            if inspect.isasyncgen(arg):
                arg = await arg.__anext__()
            new_args.append(arg)

        response = ensure_response(await next_handler(*new_args, **kwargs))

        return response

    return wrapped
