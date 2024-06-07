import httpx

from src.service.social_auth.base_social_auth import BaseSocialAuth


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
