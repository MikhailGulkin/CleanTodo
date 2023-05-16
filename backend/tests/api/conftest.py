import asyncio
from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import close_all_sessions
from src.application.common.interfaces.mapper import Mapper
from src.infrastructure.config_loader import load_config
from src.infrastructure.db import DBConfig
from src.infrastructure.db.main import build_sa_engine, build_sa_session_factory
from src.infrastructure.di import DiScope, init_di_builder, setup_di_builder
from src.infrastructure.event_bus.bindings import bind_exchanges_queue
from src.infrastructure.event_bus.exchanges import declare_exchanges
from src.infrastructure.event_bus.queues import declare_queue
from src.infrastructure.mediator import init_mediator, setup_mediator
from src.presentation.api.config import Config, setup_di_builder_config
from src.presentation.api.main import init_api

CONFIG_PATH = "./config/test-config.toml"


@pytest_asyncio.fixture(scope="session")
async def build_test_app() -> AsyncGenerator[FastAPI, Any]:
    config = load_config(Config, path=CONFIG_PATH)

    di_builder = init_di_builder()
    setup_di_builder(di_builder)
    setup_di_builder_config(di_builder, config)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(init_mediator, DiScope.APP, state=di_state)
        setup_mediator(mediator)

        async with di_builder.enter_scope(DiScope.REQUEST, state=di_state) as request_di_state:
            await di_builder.execute(declare_exchanges, DiScope.REQUEST, state=request_di_state)
            await di_builder.execute(declare_queue, DiScope.REQUEST, state=request_di_state)
            await di_builder.execute(bind_exchanges_queue, DiScope.REQUEST, state=request_di_state)

        mapper = await di_builder.execute(Mapper, DiScope.APP, state=di_state)

        app = init_api(mediator, mapper, di_builder, di_state)

        yield app


@pytest_asyncio.fixture(scope="session")
async def engine_test() -> AsyncGenerator[AsyncEngine, None]:
    yield await build_sa_engine(load_config(DBConfig, "db", path=CONFIG_PATH)).__anext__()


@pytest_asyncio.fixture(scope="session")
async def db_session_test(engine_test: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    yield build_sa_session_factory(engine_test)
    close_all_sessions()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_tables(db_session_test) -> None:
    tables = ("users",)
    async with db_session_test() as session:
        for table in tables:
            statement = text(f"""TRUNCATE TABLE {table} CASCADE;""")
            await session.execute(statement)
            await session.commit()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def client(build_test_app: FastAPI) -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=build_test_app, base_url="http://test") as client_:
        yield client_
