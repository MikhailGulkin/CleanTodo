from di import ScopeState
from didiator import CommandMediator, EventMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import FastAPI
from src.application.common.interfaces.mapper import Mapper
from src.presentation.api.providers.stub import Stub

from .di import StateProvider
from .mediator import MediatorProvider


def setup_providers(
    app: FastAPI,
    mediator: Mediator,
    mapper: Mapper,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    mediator_provider = MediatorProvider(mediator)

    app.dependency_overrides[Stub(Mediator)] = mediator_provider.build
    app.dependency_overrides[Stub(CommandMediator)] = mediator_provider.build
    app.dependency_overrides[Stub(QueryMediator)] = mediator_provider.build
    app.dependency_overrides[Stub(EventMediator)] = mediator_provider.build

    app.dependency_overrides[Stub(Mapper)] = lambda: mapper

    state_provider = StateProvider(di_state)

    app.dependency_overrides[Stub(DiBuilder)] = lambda: di_builder
    app.dependency_overrides[Stub(ScopeState)] = state_provider.build
