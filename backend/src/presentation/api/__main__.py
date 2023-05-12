from src.infrastructure.config_loader import load_config
from src.infrastructure.di import DiScope, init_di_builder, setup_di_builder
from src.infrastructure.mediator.main import init_mediator, setup_mediator
from src.presentation.api.config import Config, setup_di_builder_config
from src.presentation.api.main import init_api, run_api


async def main() -> None:
    config = load_config(Config)

    di_builder = init_di_builder()

    setup_di_builder(di_builder=di_builder)
    setup_di_builder_config(di_builder=di_builder, config=config)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(init_mediator, DiScope.APP, state=di_state)
        setup_mediator(mediator)

        app = await init_api(mediator=mediator, di_builder=di_builder, di_state=di_state)
        await run_api(app=app, config=config.api)
