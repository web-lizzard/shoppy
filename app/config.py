import logging

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    url: str = "sqlite+aiosqlite:///:memory:"
    echo_sql: bool = True


class ApiSettings(BaseModel):
    title: str = "Shoppy"
    description: str = "DDD Implementation of e-commerce shop"
    debug: bool = True


class Settings(BaseSettings):
    port: int = 8000

    database: DatabaseSettings = DatabaseSettings()
    api_settings: ApiSettings = ApiSettings()
    logging_level: int = logging.DEBUG

    class ConfigDict:
        env_nested_delimiter = "__"


settings = Settings()
