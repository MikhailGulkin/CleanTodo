from typing import Any
from uuid import UUID

from di import ScopeState
from src.infrastructure.mediator import get_mediator

from src.application.user.queries import GetUserById
from src.infrastructure.mediator.main import setup_mediator, init_mediator
from src.infrastructure.di import setup_di_builder
from src.infrastructure.di import init_di_builder, DiScope
from src.infrastructure.config_loader import load_config

from src.presentation.api.config import setup_di_builder_config
from src.presentation.api.config import Config
from src.presentation.api.main import init_api, run_api


async def main() -> None:
    config = load_config(Config)

    di_builder = init_di_builder()

    setup_di_builder(di_builder=di_builder)
    setup_di_builder_config(di_builder=di_builder, config=config)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(init_mediator, DiScope.APP, state=di_state)
        setup_mediator(mediator)

        # async with di_builder.enter_scope(DiScope.REQUEST, state=di_state) as di_req:
        #     # di_values: dict[Any, Any] = {ScopeState: di_req}
        #     mediator = mediator.bind(di_state=di_req)
        #     # di_values |= {get_mediator: mediator}
        #     user = await mediator.query(GetUserById(user_id=UUID('3fa85f64-5717-4562-b3fc-2c963f66afa5')))
        #
        #     print(user)

        app = await init_api(mediator=mediator, di_builder=di_builder, di_state=di_state)
        await run_api(app=app, config=config.api)
