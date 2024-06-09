import httpx
from starlette.responses import Response
from fastapi import HTTPException
from src.schemas.user import AddUserSchema, LoginUserSchema, UserSchema
from src.service.auth_service.auth_service import AuthService
from src.service.auth_service.jwt_auth import JWTAuth
from src.service.db_services.user_service import UserService
from src.service.social_auth.base_social_auth import BaseSocialAuth
from src.service.unit_of_work.unit_of_work import IUnitOfWork


class YandexAuth(BaseSocialAuth):
    auth_url = "https://oauth.yandex.com/authorize"
    token_url = "https://oauth.yandex.com/token"
    user_info_url = "https://login.yandex.ru/info"

    async def get_auth_url(self) -> str:
        return f"{self.auth_url}?response_type=code&client_id={self.client_id}&redirect_uri={self.redirect_uri}"

    async def get_access_token(self, code: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(self.token_url, data={
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'redirect_uri': self.redirect_uri
            })
            return response.json()

    async def get_user_info(self, token: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.user_info_url, params={'oauth_token': token})
            return response.json()

    async def register(self, uow: IUnitOfWork, token: str, response: Response):
        """
        register and login user with yandex social auth
        :param uow:
        :param token:
        :param response:
        :return: None
        """
        user_info = await self.get_user_info(token)
        user_schema = AddUserSchema(
            email=user_info['default_email'],
            password='social',
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],
            is_active=True,
            is_superuser=False
        )
        try:
            user_id = await UserService().add(uow=uow, data=user_schema)
            await JWTAuth().get_cookies(uow=uow, response=response, payload={
                "sub": str(user_id)
            })
        except HTTPException:
            await self.login(uow=uow, token=token, response=response)

    async def login(self, uow: IUnitOfWork, token: str, response: Response):
        user_info = await self.get_user_info(token)
        credentials = LoginUserSchema(
            email=user_info['default_email'],
            password='social'
        )
        await AuthService().login(uow, credentials, response)
