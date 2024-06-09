from fastapi import APIRouter
from starlette.responses import Response

from config import settings
from src.endpoints.dependencies import UnitOfWorkDependency
from src.service.social_auth.yandex_auth import YandexAuth

social_auth_router = APIRouter(tags=['yandex social authentication'])

yandex_auth = YandexAuth(settings.yandex_client_id, settings.yandex_client_secret, settings.yandex_redirect_uri)


@social_auth_router.get("/login/yandex")
async def login_yandex():
    return {"auth_url": await yandex_auth.get_auth_url()}


@social_auth_router.get("/auth/yandex/callback")
async def yandex_callback(code: str, uow: UnitOfWorkDependency, response: Response):
    token_response = await yandex_auth.get_access_token(code)
    await yandex_auth.register(uow=uow, token=token_response.get("access_token"), response=response)
