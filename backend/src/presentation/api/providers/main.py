import asyncio
from collections.abc import AsyncGenerator, Coroutine
from typing import Any

from blacksheep import Application
from di import ScopeState
from didiator import CommandMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.presentation.api.providers.di import StateProvider
from src.presentation.api.providers.mediator import MediatorProvider
from src.infrastructure.db.main import build_sa_session, build_sa_session_factory


def setup_providers(
        app: Application,
        mediator: Mediator,
        di_builder: DiBuilder,
        di_state: ScopeState
):
    provider = MediatorProvider(mediator=mediator, builder=di_builder, di_state=di_state)
    # state_provider = StateProvider(di_state=di_state)
    # di_values: dict[Any, Any] = {ScopeState: di_state}
    # mediator.bind(di_state=di_state, di_values=di_values)
    # app.services.add_instance(mediator, declared_class=Mediator)
    # app.services.add_instance(state_provider)
    # app.services.add_scoped_by_factory(state_provider.build, return_type=Mediator)
    app.services.add_scoped_by_factory(provider.build, return_type=Coroutine[Mediator])
    app.services.add_scoped_by_factory(provider.build, return_type=Coroutine[QueryMediator])
    # app.on_start += provider.build
    # app.services.add_scoped_by_factory(lambda: di_builder, return_type=DiBuilder)
    # app.services += state_provider.build
    # app.services.add_scoped_by_factory(build_sa_session_factory)
    # app.services.add_scoped_by_factory(build_sa_session, return_type=AsyncSession)
