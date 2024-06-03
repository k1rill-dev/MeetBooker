from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from src.endpoints.auth.utils import Hasher
from src.schemas.issued_tokens import IssuedTokensSchema, UpdateIssuedTokensSchema
from src.schemas.user import LoginUserSchema, UserSchema, AddUserSchema
from src.service.auth_service.jwt_auth import JWTAuth
from src.service.auth_service.types import RefreshToken
from src.service.db_services.tokens_service import TokenService
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class AuthService:
    async def authenticate_user(self, uow: IUnitOfWork, credentials: LoginUserSchema) -> UserSchema:
        res = await UserService().get_by_email(uow, credentials.email)
        if Hasher.validate_password(credentials.password, res.password):
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

    async def logout(self, uow: IUnitOfWork, response: Response, user: UserSchema):
        await TokenService().edit_multiple(uow=uow, data=UpdateIssuedTokensSchema(
            revoke=True
        ), subject=user.id)
        await JWTAuth().unset_cookies(response=response)

    async def register(self, user: AddUserSchema, uow: IUnitOfWork):
        res = await UserService().add(uow=uow, data=user)
        return res

    async def rotate_tokens(self, uow: IUnitOfWork, refresh_token: RefreshToken, response: Response):
        payload = await JWTAuth.validate_token(refresh_token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Token is invalid')
        jti = payload['jti']
        user_id = UUID(payload['sub'])
        if await TokenService().check_revoked(jti=jti, uow=uow):
            await TokenService().edit_multiple(uow, data=UpdateIssuedTokensSchema(
                revoke=True
            ), subject=user_id)
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Token already revoked')

        await JWTAuth().unset_cookies(response=response)
        device_id = payload['device_id']
        await TokenService().edit_multiple(uow, data=UpdateIssuedTokensSchema(revoke=True), subject=user_id,
                                           device_id=device_id)

        encoded_data = {
            "sub": str(user_id)
        }
        await JWTAuth().get_cookies(response=response, payload=encoded_data, uow=uow)
