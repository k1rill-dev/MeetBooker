from fastapi import APIRouter

from config import settings
from src.service.social_auth.vk_auth import VKAuth

vk_router = APIRouter(tags=['vk social auth'])

vk_auth = VKAuth(settings.vk_client_id, settings.vk_client_secret, settings.vk_redirect_uri)


@vk_router.get("/login/vk")
async def login_vk():
    return {"auth_url": await vk_auth.get_auth_url()}


@vk_router.get("/auth/vk/callback")
async def vk_callback(code: str):
    token_response = await vk_auth.get_access_token(code)
    user_info = await vk_auth.get_user_info(token_response.get('access_token'))
    return user_info
