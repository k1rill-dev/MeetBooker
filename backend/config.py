import os
from envparse import Env
from pydantic_settings import BaseSettings

env = Env()

env.read_envfile()


class Settings(BaseSettings):
    db_url: str = env.str('DATABASE_URL', default='postgresql+asyncpg://postgres:lolkek123@localhost:5432/postgres')


settings = Settings()
