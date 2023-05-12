from dataclasses import dataclass

from blacksheep.server.controllers import get
from src.presentation.api.conrtollers.base_contoller import BaseAPIController
from src.presentation.api.conrtollers.docs import get_healthcheck_docs
from src.presentation.api.docs import docs


@dataclass(frozen=True)
class OkStatus:
    status: str = "ok"


class HealthCheck(BaseAPIController):
    def __init__(self):
        self.status = OkStatus()

    @docs(get_healthcheck_docs)
    @get("/")
    async def get_status(self) -> OkStatus:
        return self.status
