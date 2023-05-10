import uvicorn
from blacksheep.server import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v2 import Info

from src.presentation.api.docs import docs
from src.presentation.api import conrtollers  # noqa


async def init_api() -> Application:
    app = Application()

    # setup_controllers(app=app)

    docs.bind_app(app)

    return app


async def run_api(app: Application) -> None:
    config = uvicorn.Config(app, host='127.0.0.1', port=8000)
    server = uvicorn.Server(config)
    await server.serve()
