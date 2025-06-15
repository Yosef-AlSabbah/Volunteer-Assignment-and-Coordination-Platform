from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import List

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env', env_file_encoding='utf-8', extra='ignore')

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    DJANGO_SECRET_KEY: str
    DJANGO_DEBUG: bool = True
    DJANGO_ALLOWED_HOSTS: List[str] = ['localhost', '127.0.0.1']


settings = Settings()

