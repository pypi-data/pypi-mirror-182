from functools import lru_cache

from pydantic import BaseSettings, FilePath


class Settings(BaseSettings):
    """A global settings object for the application. Containing the notebook path."""

    notebook_path: FilePath

    class Config:  # noqa: D106
        env_file = ".env"


@lru_cache
def get_settings():
    """Gets the settings currently in use by the application."""
    return Settings()
