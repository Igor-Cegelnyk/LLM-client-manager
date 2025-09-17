from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

BASE_DIR = Path(__file__).parent.parent.parent


class RunConfig(BaseModel):
    host: str
    port: int


class ApiPrefix(BaseModel):
    generate: str = "/generate"


class OllamaClientConfig(BaseSettings):
    url: str
    model: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env.template",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    run: RunConfig
    api_prefix: ApiPrefix = ApiPrefix()
    ollama_client_config: OllamaClientConfig


settings = Settings()
