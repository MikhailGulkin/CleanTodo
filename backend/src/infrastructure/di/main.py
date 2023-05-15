from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import AsyncExecutor
from didiator.interface.utils.di_builder import DiBuilder
from didiator.utils.di_builder import DiBuilderImpl
from sqlalchemy.ext.asyncio import (  # noqa di conflict with aio_pika and sqlalchemy
    async_sessionmaker,
)
from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.di import DiScope
from src.infrastructure.di.factories import (
    setup_db_factories,
    setup_event_bus_factories,
    setup_mediator_factory,
)
from src.infrastructure.mapper.main import build_mapper
from src.infrastructure.mediator.stub import get_mediator
from src.infrastructure.uow import build_uow


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = [DiScope.APP, DiScope.REQUEST]
    di_builder = DiBuilderImpl(di_container, di_executor, di_scopes=di_scopes)
    return di_builder


def setup_di_builder(di_builder: DiBuilder) -> None:
    di_builder.bind(bind_by_type(Dependent(lambda *args: di_builder, scope=DiScope.APP), DiBuilder))
    di_builder.bind(bind_by_type(Dependent(build_mapper, scope=DiScope.APP), Mapper))
    di_builder.bind(bind_by_type(Dependent(build_uow, scope=DiScope.REQUEST), UnitOfWork))

    setup_mediator_factory(di_builder, get_mediator, DiScope.REQUEST)
    setup_db_factories(di_builder)
    setup_event_bus_factories(di_builder)
