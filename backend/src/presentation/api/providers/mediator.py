from typing import Any

from di import ScopeState
from didiator import Mediator
from src.infrastructure.mediator import get_mediator


class MediatorProvider:
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    async def build(self, di_state: ScopeState) -> Mediator:
        di_values: dict[Any, Any] = {ScopeState: di_state}
        mediator = self._mediator.bind(di_state=di_state, di_values=di_values)
        di_values |= {get_mediator: mediator}
        return mediator
