from fastapi import APIRouter
from src.endpoints.auth.utils import Hasher
from src.endpoints.dependencies import UnitOfWorkDependency
from src.schemas.user import LoginUserSchema, UserSchema
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork

login_router = APIRouter(tags=["login"])


async def _authenticate_user(uow: IUnitOfWork, credentials: LoginUserSchema) -> UserSchema:
    res = await UserService().get_by_email(uow, credentials.email)
    if Hasher.validate_password(res.password, credentials.password):
        return res


@login_router.post("/login")
async def login(user: LoginUserSchema, uow: UnitOfWorkDependency):
    authenticated_user = await _authenticate_user(uow, user)
    """TODO: генерируем токены и возвращаем в куки"""
    return authenticated_user
