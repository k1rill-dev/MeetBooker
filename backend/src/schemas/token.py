from pydantic import BaseModel

from src.service.auth_service.types import AccessToken, RefreshToken


class TokensSchema(BaseModel):
    access_token: AccessToken
    refresh_token: RefreshToken

    class Config:
        from_attributes = True
