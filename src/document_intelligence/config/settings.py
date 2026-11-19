""" Centralized application configuration"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ Application settings loaded from environment variables and env"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    app_name: str = Field(
        default="Document Intelligence System",
        description="Application display name."
    )

    log_env: str = Field(
        default="development",
        description="Application execution environment"
    )

    log_level: str = Field(
        default="INFO",
        description="Application logging level."
    )

@lru_cache
def get_settings() -> Settings:
    """Return a cached application settings instance"""
    return Settings()