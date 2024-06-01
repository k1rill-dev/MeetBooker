from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from src.endpoints.auth.utils import Hasher
from src.schemas.issued_tokens import IssuedTokensSchema
from src.schemas.user import LoginUserSchema, UserSchema, AddUserSchema
from src.service.auth_service.jwt_auth import JWTAuth
from src.service.db_services.tokens_service import TokenService
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AuthService:
    async def authenticate_user(self, uow: IUnitOfWork, credentials: LoginUserSchema) -> UserSchema:
        res = await UserService().get_by_email(uow, credentials.email)
        if Hasher.validate_password(res.password, credentials.password):
            return res

    async def login(self, uow: IUnitOfWork, credentials: LoginUserSchema, response: Response) -> UserSchema:
        user = await self.authenticate_user(uow, credentials)
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User does not exist')
        payload = {
            "sub": str(user.id)
        }
        await JWTAuth().get_cookies(response=response, payload=payload, uow=uow)
        return user

    async def logout(self, uow: IUnitOfWork, response: Response):
        """отозвать все токены"""
        await JWTAuth().unset_cookies(response=response)

    async def register(self, user: AddUserSchema, uow: IUnitOfWork):
        res = await UserService().add(uow=uow, data=user)
        return res
