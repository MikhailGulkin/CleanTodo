from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from src.infrastructure.di import DiScope


class MediatorProvider:
    def __init__(self, mediator: Mediator, builder: DiBuilder, di_state: ScopeState) -> None:
        self._mediator = mediator
        self._builder = builder
        self._state = di_state

    async def build(self) -> Mediator:
        async with self._builder.enter_scope(DiScope.REQUEST, state=self._state) as di_req:
            mediator = self._mediator.bind(di_state=di_req)
            yield mediator
