from di import ScopeState
from didiator import CommandMediator, EventMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import FastAPI
from src.application.common.interfaces.mapper import Mapper

from .di import StateProvider, get_di_builder, get_di_state
from .mediator import MediatorProvider


def setup_providers(
    app: FastAPI,
    mediator: Mediator,
    mapper: Mapper,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    mediator_provider = MediatorProvider(mediator)

    app.dependency_overrides[Mediator] = mediator_provider.build
    app.dependency_overrides[CommandMediator] = mediator_provider.build
    app.dependency_overrides[QueryMediator] = mediator_provider.build
    app.dependency_overrides[EventMediator] = mediator_provider.build

    app.dependency_overrides[Mapper] = lambda: mapper

    state_provider = StateProvider(di_state)

    app.dependency_overrides[get_di_builder] = lambda: di_builder
    app.dependency_overrides[get_di_state] = state_provider.build
