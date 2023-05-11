from collections.abc import AsyncGenerator
from typing import Any

import rodi
from blacksheep import Application
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from rodi import GetServiceContext

from src.infrastructure.di import DiScope
from src.infrastructure.mediator import get_mediator

from .di import get_di_state


class MediatorProvider:
    def __init__(self, mediator: Mediator, builder: DiBuilder, di_state: ScopeState) -> None:
        self._mediator = mediator
        self._builder = builder
        self._state = di_state

    async def build(self) -> Mediator:
        async with self._builder.enter_scope(DiScope.REQUEST, state=self._state) as di_req:
            # di_values: dict[Any, Any] = {ScopeState: di_req}
            mediator = self._mediator.bind(di_state=di_req)
            return mediator
            # di_values |= {get_mediator: mediator}
        # di_state: AsyncGenerator[[DiBuilder], ScopeState] = rodi_service.provider.get(ScopeState)
        # di_state = await di_state.__anext__()
        # # print(rodi_service, di_state, type(di_state) == ScopeState)
        # di_values: dict[Any, Any] = {ScopeState: di_state}
        # mediator = self._mediator.bind(di_state=di_state, di_values=di_values)
        # di_values |= {get_mediator: mediator}
        # return self._mediator
