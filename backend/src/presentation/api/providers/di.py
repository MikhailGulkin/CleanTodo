from collections.abc import AsyncGenerator

from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import Depends
from src.infrastructure.di import DiScope

from .stub import Stub


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None):
        self._di_state = di_state

    async def build(
        self,
        di_builder: DiBuilder = Depends(Stub(DiBuilder)),
    ) -> AsyncGenerator[DiBuilder, ScopeState]:
        async with di_builder.enter_scope(DiScope.REQUEST, self._di_state) as di_state:
            yield di_state
