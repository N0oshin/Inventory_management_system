from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings managed with Pydantic."""

    # Database
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
