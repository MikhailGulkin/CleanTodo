import aio_pika
from aio_pika.abc import AbstractChannel
from src.infrastructure.message_broker import ConfigurateMessageBroker


class ConfigurateMessageBrokerImpl(ConfigurateMessageBroker):
    def __init__(self, channel: AbstractChannel) -> None:
        self._channel = channel

    async def declare_exchange(self, exchange_name: str) -> None:
        await self._channel.declare_exchange(exchange_name, aio_pika.ExchangeType.TOPIC)

    async def declare_queue(self, queue_name: str) -> None:
        await self._channel.declare_queue(name=queue_name, durable=True)

    async def bind_exchange_queue(self, exchange_name: str, queue_name: str, routing_key) -> None:
        exchange = await self._channel.get_exchange(exchange_name, ensure=True)
        queue = await self._channel.get_queue(queue_name, ensure=True)
        await queue.bind(exchange, routing_key=routing_key)
