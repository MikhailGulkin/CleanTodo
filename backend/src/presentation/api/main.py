import uvicorn
from blacksheep.server import Application
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder

from src.presentation.api.config import APIConfig
from src.presentation.api.providers.main import setup_providers
from src.presentation.api.docs import docs
from src.presentation.api import conrtollers  # noqa


async def init_api(mediator: Mediator, di_builder: DiBuilder, di_state: ScopeState | None = None) -> Application:
    app = Application()

    setup_providers(app=app, mediator=mediator, di_state=di_state, di_builder=di_builder)
    docs.bind_app(app)

    return app


async def run_api(app: Application, config: APIConfig) -> None:
    config = uvicorn.Config(
        app=app,
        host=config.host,
        port=config.port,
    )
    server = uvicorn.Server(config)
    await server.serve()
