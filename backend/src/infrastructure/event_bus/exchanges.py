from src.infrastructure.message_broker import ConfigurateMessageBroker

USER_EXCHANGE = "users"


async def declare_exchanges(configurate_broker: ConfigurateMessageBroker) -> None:
    await configurate_broker.declare_exchange(USER_EXCHANGE)
