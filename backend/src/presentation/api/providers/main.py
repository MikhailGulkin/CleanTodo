from di import ScopeState
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import Depends, FastAPI
from src.application.common.interfaces.mapper import Mapper
from src.application.user.commands.create_user import BaseCreateUserHandler
from src.infrastructure.di import DiScope
from src.presentation.api.providers.stub import Stub

from .di import StateProvider


def setup_providers(
    app: FastAPI,
    mapper: Mapper,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
) -> None:
    async def get_create_user_handler(
        state: ScopeState = Depends(Stub(ScopeState)), builder: DiBuilder = Depends(Stub(DiBuilder))
    ) -> BaseCreateUserHandler:
        return await builder.execute(BaseCreateUserHandler, scope=DiScope.REQUEST, state=state)

    # app.dependency_overrides[Stub(GetUserByUsernameHandler)] = lambda: GetUserByUsernameHandler
    app.dependency_overrides[Stub(BaseCreateUserHandler)] = get_create_user_handler
    # app.dependency_overrides[Stub(GetUserByIdHandler)] = lambda: GetUserByIdHandler

    app.dependency_overrides[Stub(Mapper)] = lambda: mapper

    state_provider = StateProvider(di_state)

    app.dependency_overrides[Stub(DiBuilder)] = lambda: di_builder
    app.dependency_overrides[Stub(ScopeState)] = state_provider.build
