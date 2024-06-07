import os
import pathlib
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

load_dotenv(str(BASE_DIR / '.env'))


class Settings(BaseSettings):
    db_url: str = os.getenv('DATABASE_URL', default='postgresql+asyncpg://postgres:lolkek123@localhost:5432/postgres')
    private_key: str = BASE_DIR.joinpath('backend/src/certs/jwt-private.pem').read_text()
    public_key: str = BASE_DIR.joinpath('backend/src/certs/jwt-public.pem').read_text()
    access_token_expires_minutes: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', default=15)
    refresh_token_expires_days: int = os.getenv('REFRESH_TOKEN_EXPIRE_DAYS', default=30)
    jwt_algorithm: str = os.getenv('JWT_ALGORITHM', default='RS256')
    path_to_media: pathlib.Path = BASE_DIR.joinpath('backend/media/')
    yandex_client_id: str
    yandex_client_secret: str
    yandex_redirect_uri: str


settings = Settings()
