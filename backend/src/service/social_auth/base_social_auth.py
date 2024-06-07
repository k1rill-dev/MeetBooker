from abc import ABC, abstractmethod


class BaseSocialAuth(ABC):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    @abstractmethod
    async def get_auth_url(self) -> str:
        pass

    @abstractmethod
    async def get_access_token(self, code: str) -> dict:
        pass

    @abstractmethod
    async def get_user_info(self, token: str) -> dict:
        pass
