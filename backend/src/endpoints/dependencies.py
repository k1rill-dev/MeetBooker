from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, Cookie
from starlette import status

from config import settings
from src.service.auth_service.types import TokenTypes, AccessToken
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork, UnitOfWork

UnitOfWorkDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]


async def get_user_from_token(uow: UnitOfWorkDependency, access_token: AccessToken = Cookie(...)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
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
    if user is None:
        raise credentials_exception
    return user
