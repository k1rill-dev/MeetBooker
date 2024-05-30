import pathlib

from envparse import Env
from pydantic_settings import BaseSettings

env = Env()

env.read_envfile()


class Settings(BaseSettings):
    db_url: str = env.str('DATABASE_URL', default='postgresql+asyncpg://postgres:lolkek123@localhost:5432/postgres')
    private_key: str = pathlib.Path(__file__).parent.joinpath('src/certs/jwt-private.pem').read_text()
    public_key: str = pathlib.Path(__file__).parent.joinpath('src/certs/jwt-public.pem').read_text()


settings = Settings()
