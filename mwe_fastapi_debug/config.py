"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_PORT: int = 8000
    APP_HOST: str = "0.0.0.0"
    DEBUGGER_HOST: str = "0.0.0.0"
    DEBUGGER_PORT: int = 5678
    PYCHARM_DEBUGGER: bool = False
    PYCHARM_DEBUGGER_PATH: str = "/app/pydevd-pycharm.egg"


settings = Settings()
