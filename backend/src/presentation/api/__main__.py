from src.presentation.api.main import init_api, run_api


async def main() -> None:
    app = await init_api()
    await run_api(app=app)
