from dataclasses import dataclass

from fastapi import status
from sanic import Blueprint, HTTPResponse
from sanic.response.types import Request

healthcheck_router = Blueprint(
    name="healthcheck",
    url_prefix="/healthcheck",
)


@dataclass(frozen=True)
class OkStatus:
    status: str = "ok"


OK_STATUS = OkStatus()


@healthcheck_router.get("/")
async def get_status(_: Request) -> HTTPResponse:
    return HTTPResponse(status=status.HTTP_200_OK, body=OK_STATUS.status)
