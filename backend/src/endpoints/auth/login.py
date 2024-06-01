from fastapi import APIRouter
from starlette.responses import Response

from src.endpoints.dependencies import UnitOfWorkDependency
from src.schemas.user import LoginUserSchema
from src.service.auth_service.auth_service import AuthService

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/login")
async def login(user: LoginUserSchema, uow: UnitOfWorkDependency, response: Response):
    authenticated_user = await AuthService().authenticate_user(uow, user)
    await AuthService().login(uow=uow, credentials=user, response=response)
    return authenticated_user


@auth_router.post("/logout")
async def logout(uow: UnitOfWorkDependency):
    """
    логаут пользователя, отзываем все токены пользователя
    """
    pass
