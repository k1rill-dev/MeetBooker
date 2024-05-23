import os
from envparse import Env
from pydantic_settings import BaseSettings

env = Env()

env.read_envfile()


class Settings(BaseSettings):
    db_url: str = env.str('DATABASE_URL', default='sqlite:///db.sqlite3')


settings = Settings()
