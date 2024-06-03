import enum
import uuid
from datetime import datetime, timedelta
from http.client import HTTPException

import jwt
from fastapi import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from config import settings
from src.schemas.issued_tokens import IssuedTokensSchema
from src.schemas.token import TokensSchema
from src.service.auth_service.types import AccessToken, Token, RefreshToken, TokenTypes
from src.service.db_services.tokens_service import TokenService
from src.service.db_services.user_service import UserService
from src.service.unit_of_work.unit_of_work import IUnitOfWork, UnitOfWork


class JWTAuth:
    async def __gen_device_id(self):
        return uuid.uuid4()

    async def _create_token(self, payload: dict, uow: IUnitOfWork, expires_at: int, token_type: str) -> Token:
        """
        Создает JWT токен
        :param payload: показывает, что будет лежать в токене
        :param uow: Unit of Work зависимость
        :param expires_at: когда токен перестает "жить"
        :param token_type: вид токена(refresh|access_token)
        :return: Токен
        """
        # todo: перенести expires_at в конфиг, дабы избежать повторения кода
        expires_at = datetime.utcnow() + timedelta(
            days=expires_at) if token_type != TokenTypes.ACCESS_TOKEN.value else datetime.utcnow() + timedelta(
            minutes=expires_at)
        to_encode = payload.copy()
        to_encode.update({
            "type": token_type,
            "exp": expires_at,
            "iat": datetime.utcnow(),
            "jti": str(uuid.uuid4()),
            "device_id": str(await self.__gen_device_id()),
        })
        encoded_token = jwt.encode(to_encode, settings.private_key, algorithm=settings.jwt_algorithm)
        data = IssuedTokensSchema(
            id=to_encode["jti"],
            subject=uuid.UUID(to_encode['sub']),
            device_id=to_encode['device_id'],
            revoke=False
        )
        _ = await TokenService().add(uow=uow, data=data)
        return encoded_token

    async def _get_tokens(self, payload: dict, uow: IUnitOfWork) -> TokensSchema:
        """
        Создает access- и refresh- токены
        :param payload: что будет лежать в токенах
        :param uow: Unit of Work зависимость
        :return: возвращает пару токенов
        """
        access_token = await self._create_token(payload, uow, settings.access_token_expires_minutes,
                                                TokenTypes.ACCESS_TOKEN.value)
        refresh_token = await self._create_token(payload, uow, settings.refresh_token_expires_days,
                                                 TokenTypes.REFRESH_TOKEN.value)
        return TokensSchema(access_token=access_token, refresh_token=refresh_token)

    async def _set_cookies(self, response: Response, tokens: TokensSchema, user_id: uuid.UUID):
        """
        устанавливает cookie в response
        :param response: response из FastAPI
        :param tokens: токены
        :return: None
        """
        response.set_cookie("access_token", tokens.access_token, httponly=True)
        response.set_cookie("refresh_token", tokens.refresh_token, httponly=True)
        response.set_cookie("login", str(user_id))

    async def unset_cookies(self, response: Response):
        response.delete_cookie("login")
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

    async def get_cookies(self, response: Response, payload: dict, uow: IUnitOfWork):
        """
        возвращает access- и refresh- токены в cookie
        :param response: FastAPI response
        :param payload: данные в токене
        :param uow: Unit of Work зависимость
        :return: None
        """
        tokens = await self._get_tokens(payload, uow)
        await self._set_cookies(response, tokens, payload["sub"])

    @staticmethod
    async def validate_token(token: Token) -> dict:
        try:
            payload = jwt.decode(token, settings.public_key, algorithms=[settings.jwt_algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Token is expired"
            )

    async def rotate_tokens(self, response: Response, refresh_token: RefreshToken, uow: IUnitOfWork):
        payload = await JWTAuth.validate_token(refresh_token)
        if payload['type'] != TokenTypes.REFRESH_TOKEN.value:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                                detail="Get access token, not refresh token")
        tokens = await TokenService().list(uow, subject=payload["sub"])
        await self.unset_cookies(response)
        await self.get_cookies(response, payload, uow)
