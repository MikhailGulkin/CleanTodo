from src.infrastructure.event_bus.events import EVENT_CREATE
from src.infrastructure.message_broker import ConfigurateMessageBroker

from .exchanges import USER_EXCHANGE
from .queues import USER_QUEUE


async def bind_exchanges_queue(configurate_broker: ConfigurateMessageBroker) -> None:
    await configurate_broker.bind_exchange_queue(
        exchange_name=USER_EXCHANGE, queue_name=USER_QUEUE, routing_key=EVENT_CREATE
    )
