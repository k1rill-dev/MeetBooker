from fastapi import APIRouter

from src.endpoints.dependencies import UnitOfWorkDependency
from src.schemas.user import AddUserSchema
from src.service.db_services.user_service import UserService

register_router = APIRouter(tags=["register"])


@register_router.post("/register")
async def register_user(user: AddUserSchema, uow: UnitOfWorkDependency):
    res = await UserService().add(uow=uow, data=user)
    return {"res": res}
