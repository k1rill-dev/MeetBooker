import httpx

from src.service.social_auth.base_social_auth import BaseSocialAuth


class VKAuth(BaseSocialAuth):
    auth_url = "https://oauth.vk.com/authorize"
    token_url = "https://oauth.vk.com/access_token"
    user_info_url = "https://api.vk.com/method/users.get"

    async def get_auth_url(self) -> str:
        return f"{self.auth_url}?client_id={self.client_id}&display=page&redirect_uri={self.redirect_uri}&scope=email&response_type=code&v=5.131"

    async def get_access_token(self, code: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.token_url, params={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'redirect_uri': self.redirect_uri,
                'code': code
            })
            return response.json()

    async def get_user_info(self, token: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.user_info_url, params={
                'access_token': token,
                'v': '5.131'
            })
            return response.json()
