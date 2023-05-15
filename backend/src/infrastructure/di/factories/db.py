from di import bind_by_type
from di.dependent import Dependent
from didiator.interface.utils.di_builder import DiBuilder
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from src.application.user.interfaces import UserReader, UserRepo
from src.infrastructure.db.main import (
    build_sa_engine,
    build_sa_session,
    build_sa_session_factory,
)
from src.infrastructure.db.repositories import UserReaderImpl, UserRepoImpl
from src.infrastructure.di import DiScope


def setup_db_factories(di_builder: DiBuilder) -> None:
    di_builder.bind(bind_by_type(Dependent(build_sa_engine, scope=DiScope.APP), AsyncEngine))
    di_builder.bind(
        bind_by_type(
            Dependent(build_sa_session_factory, scope=DiScope.APP),
            async_sessionmaker[AsyncSession],
        )
    )
    di_builder.bind(bind_by_type(Dependent(build_sa_session, scope=DiScope.REQUEST), AsyncSession))
    di_builder.bind(bind_by_type(Dependent(UserRepoImpl, scope=DiScope.REQUEST), UserRepo, covariant=True))
    di_builder.bind(
        bind_by_type(
            Dependent(UserReaderImpl, scope=DiScope.REQUEST),
            UserReader,
            covariant=True,
        )
    )
