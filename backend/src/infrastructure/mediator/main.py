from didiator import CommandDispatcherImpl, EventObserverImpl, Mediator, MediatorImpl, QueryDispatcherImpl
from didiator.middlewares.di import DiMiddleware, DiScopes

from didiator.interface.utils.di_builder import DiBuilder

from src.application.user.commands import CreateUser, CreateUserHandler

from src.application.user.queries import GetUserById, GetUserByIdHandler, GetUserByUsername, GetUserByUsernameHandler
# from src.application.user.queries.get_users import GetUsers, GetUsersHandler
from src.domain.common.events import Event
from src.infrastructure.di import DiScope
from src.infrastructure.event_bus.event_handler import EventHandlerPublisher


def init_mediator(di_builder: DiBuilder) -> Mediator:
    middlewares = (
        DiMiddleware(di_builder, scopes=DiScopes(DiScope.REQUEST)),
    )
    command_dispatcher = CommandDispatcherImpl(middlewares=middlewares)
    query_dispatcher = QueryDispatcherImpl(middlewares=middlewares)
    event_observer = EventObserverImpl(middlewares=middlewares)

    mediator = MediatorImpl(command_dispatcher, query_dispatcher, event_observer)
    return mediator


def setup_mediator(mediator: Mediator) -> None:
    mediator.register_command_handler(CreateUser, CreateUserHandler)
    mediator.register_query_handler(GetUserById, GetUserByIdHandler)
    mediator.register_query_handler(GetUserByUsername, GetUserByUsernameHandler)
    mediator.register_event_handler(Event, EventHandlerPublisher)
