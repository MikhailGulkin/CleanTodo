from dataclasses import dataclass
from uuid import UUID

from src.infrastructure.event_bus.exchanges import USER_EXCHANGE

from .base import IntegrationEvent, integration_event


@dataclass(frozen=True)
@integration_event("UserCreated", exchange=USER_EXCHANGE)
class UserCreated(IntegrationEvent):  # noqa
    user_id: UUID
    username: str
    password: str
    email: str
