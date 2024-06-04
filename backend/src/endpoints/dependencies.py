from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, Cookie
from starlette import status

from config import settings
from src.schemas.specialists import SpecialistSchema
from src.schemas.user import UserSchema
from src.service.auth_service.types import TokenTypes, AccessToken
from src.service.db_services.specialist_service import SpecialistService
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork, UnitOfWork

UnitOfWorkDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)


async def _get_user(access_token: AccessToken, uow: IUnitOfWork) -> UserSchema:
    try:
        payload = jwt.decode(
            access_token, settings.public_key, algorithms=[settings.jwt_algorithm]
        )
        pk: UUID = payload.get("sub")
        if pk is None:
            raise credentials_exception
        if payload.get("type") == TokenTypes.REFRESH_TOKEN.value:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    user = await UserService().get(uow, id=pk)
    return user


async def get_user_from_token(uow: UnitOfWorkDependency, access_token: AccessToken = Cookie(...)):
    user = await _get_user(access_token, uow)
    if user is None:
        raise credentials_exception
    return user


async def get_specialist_from_token(uow: UnitOfWorkDependency,
                                    access_token: AccessToken = Cookie(...)) -> SpecialistSchema:
    user = await _get_user(access_token, uow)
    if user is None:
        raise credentials_exception
    specialist = await SpecialistService().get_by_user_id(uow=uow, user_id=user.id)
    if specialist is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You not specialist",
        )
    return specialist
