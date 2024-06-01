import pathlib

from envparse import Env
from pydantic_settings import BaseSettings

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

env = Env()

env.read_envfile(BASE_DIR.joinpath('backend/.env'))


class Settings(BaseSettings):
    db_url: str = env.str('DATABASE_URL', default='postgresql+asyncpg://postgres:lolkek123@localhost:5432/postgres')
    private_key: str = BASE_DIR.joinpath('backend/src/certs/jwt-private.pem').read_text()
    public_key: str = BASE_DIR.joinpath('backend/src/certs/jwt-public.pem').read_text()
    access_token_expires_minutes: int = env.int('ACCESS_TOKEN_EXPIRE_MINUTES', default=15)
    refresh_token_expires_days: int = env.int('REFRESH_TOKEN_EXPIRE_DAYS', default=30)
    jwt_algorithm: str = env.str('JWT_ALGORITHM', default='RS256')


settings = Settings()
