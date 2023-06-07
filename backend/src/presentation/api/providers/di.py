from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder
from src.infrastructure.di import DiScope


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None):
        self._di_state = di_state

    async def build(
        self,
        di_builder: DiBuilder,
    ) -> ScopeState:
        async with di_builder.enter_scope(DiScope.REQUEST, self._di_state) as di_state:
            return di_state
