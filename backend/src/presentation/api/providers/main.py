from blacksheep import Application
from di import ScopeState
from didiator import CommandMediator, Mediator, QueryMediator
from didiator.interface.utils.di_builder import DiBuilder
from src.presentation.api.providers.mediator import MediatorProvider


def setup_providers(app: Application, mediator: Mediator, di_builder: DiBuilder, di_state: ScopeState):
    provider = MediatorProvider(mediator=mediator, builder=di_builder, di_state=di_state)

    app.services.add_scoped_by_factory(provider.build, return_type=Mediator)
    app.services.add_scoped_by_factory(provider.build, return_type=QueryMediator)
    app.services.add_scoped_by_factory(provider.build, return_type=CommandMediator)
