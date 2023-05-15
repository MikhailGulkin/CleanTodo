from typing import Any

from di import ScopeState
from didiator import Mediator
from fastapi import Depends
from src.infrastructure.mediator import get_mediator

from .stub import Stub


class MediatorProvider:
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    async def build(self, di_state: ScopeState = Depends(Stub(ScopeState))) -> Mediator:
        di_values: dict[Any, Any] = {ScopeState: di_state}
        mediator = self._mediator.bind(di_state=di_state, di_values=di_values)
        di_values |= {get_mediator: mediator}
        return mediator
