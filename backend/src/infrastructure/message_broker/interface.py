from typing import Protocol

from .message import Message


class MessageBroker(Protocol):
    async def publish_message(
        self,
        message: Message,
        routing_key: str,
        exchange_name: str,
    ) -> None:
        raise NotImplementedError


class ConfigurateMessageBroker(Protocol):
    async def declare_exchange(self, exchange_name: str) -> None:
        raise NotImplementedError

    async def declare_queue(self, queue_name: str) -> None:
        raise NotImplementedError

    async def bind_exchange_queue(self, exchange_name: str, queue_name: str, routing_key) -> None:
        raise NotImplementedError
