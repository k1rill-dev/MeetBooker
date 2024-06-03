import enum
from typing import NewType, Union

Token = NewType('Token', str)
AccessToken = NewType('AccessToken', Token)
RefreshToken = NewType('RefreshToken', Token)


class TokenTypes(enum.Enum):
    ACCESS_TOKEN = 'access_token'
    REFRESH_TOKEN = 'refresh_token'
