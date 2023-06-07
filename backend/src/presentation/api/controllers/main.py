from sanic import Sanic

from .default import default_router
from .healthcheck import healthcheck_router
from .user import user_router


def setup_controllers(app: Sanic) -> None:
    app.blueprint(default_router)
    app.blueprint(healthcheck_router)
    app.blueprint(user_router)
    # setup_exception_handlers(app)
