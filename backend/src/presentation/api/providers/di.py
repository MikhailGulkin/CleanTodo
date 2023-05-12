from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from rodi import GetServiceContext
from src.infrastructure.di import DiScope


def get_di_builder() -> DiBuilder:
    raise NotImplementedError


def get_di_state() -> ScopeState:
    raise NotImplementedError


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None):
        self._di_state = di_state

    async def build(self, rodi_service: GetServiceContext) -> Mediator:
        di_builder = rodi_service.provider.get(DiBuilder)
        async with di_builder.enter_scope(DiScope.REQUEST, self._di_state) as di_state:
            yield di_state
