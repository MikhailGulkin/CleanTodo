from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from sanic import Sanic
from src.application.common.interfaces.mapper import Mapper
from src.presentation.api.controllers import setup_controllers
from src.presentation.api.middlewares import setup_middlewares
from src.presentation.api.providers import setup_providers

from .config import APIConfig


def init_api(
    mediator: Mediator,
    mapper: Mapper,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
    debug: bool = __debug__,
) -> Sanic:
    app = Sanic(name="CleanTodo")
    setup_providers(app, mediator, mapper, di_builder, di_state)
    setup_middlewares(app)
    setup_controllers(app)
    return app


async def conf_api(app: Sanic, api_config: APIConfig) -> Sanic:
    app.prepare(host=api_config.host, port=api_config.port)
    return app
    # config = uvicorn.Config(app, )
    # server = uvicorn.Server(config)
    #
    # await server.serve()
