from src.infrastructure.message_broker import ConfigurateMessageBroker

USER_QUEUE = "users"


async def declare_queue(configurate_broker: ConfigurateMessageBroker) -> None:
    await configurate_broker.declare_queue(USER_QUEUE)
