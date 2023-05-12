from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime
from typing import TypeVar
from uuid import UUID

from uuid6 import uuid7


@dataclass(frozen=True, kw_only=True)
class IntegrationEvent:
    event_id: UUID = field(default_factory=uuid7)
    event_timestamp: datetime = field(default_factory=datetime.utcnow)
    _exchange_name: str = field(init=False)
    _routing_key: str = field(init=False)


EventType = TypeVar("EventType", bound=type[IntegrationEvent])


def integration_event(
    event_type: str,
    exchange: str | None = None,
    routing_key: str | None = None,
) -> Callable[[EventType], EventType]:
    def _integration_event(cls: EventType) -> EventType:
        cls.event_type = event_type  # type: ignore[attr-defined]
        cls._exchange_name = exchange
        cls._routing_key = routing_key if routing_key is not None else event_type
        return cls

    return _integration_event
