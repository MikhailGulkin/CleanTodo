from di import ScopeState
from didiator import CommandMediator, EventMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from sanic import Sanic
from src.application.common.interfaces.mapper import Mapper

from .di import StateProvider
from .mediator import MediatorProvider


def setup_providers(
    app: Sanic,
    mediator: Mediator,
    mapper: Mapper,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    mediator_provider = MediatorProvider(mediator)

    app.ext.add_dependency(Mediator, mediator_provider.build)
    app.ext.add_dependency(CommandMediator, mediator_provider.build)
    app.ext.add_dependency(QueryMediator, mediator_provider.build)
    app.ext.add_dependency(EventMediator, mediator_provider.build)

    app.ext.add_dependency(Mapper, lambda: mapper)

    state_provider = StateProvider(di_state)

    app.ext.add_dependency(DiBuilder, lambda: di_builder)
    app.ext.add_dependency(ScopeState, state_provider.build)
