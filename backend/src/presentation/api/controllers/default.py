from sanic import Blueprint, Request, redirect
from sanic_ext.extensions.openapi import openapi
from starlette import status

default_router = Blueprint(
    name="default_rout",
    url_prefix="",
)


@default_router.get(
    "/",
)
@openapi.exclude(True)
async def default_redirect(_: Request) -> redirect:
    return redirect(
        "/docs/swagger",
        status=status.HTTP_302_FOUND,
    )
