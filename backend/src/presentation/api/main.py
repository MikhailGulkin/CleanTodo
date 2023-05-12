import uvicorn
from blacksheep.server import Application
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from src.presentation.api import conrtollers  # noqa
from src.presentation.api.config import APIConfig
from src.presentation.api.conrtollers import setup_exception_handlers
from src.presentation.api.docs import docs
from src.presentation.api.middlwares import setup_middlewares
from src.presentation.api.providers import setup_providers


async def init_api(mediator: Mediator, di_builder: DiBuilder, di_state: ScopeState | None = None) -> Application:
    app = Application(show_error_details=True)

    setup_providers(app=app, mediator=mediator, di_state=di_state, di_builder=di_builder)
    setup_exception_handlers(app=app)
    setup_middlewares(app=app)
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
