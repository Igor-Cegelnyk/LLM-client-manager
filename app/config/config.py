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


class MockClientConfig(BaseSettings):
    registration_name: str


class OllamaClientConfig(BaseSettings):
    registration_name: str
    url: str
    model: str


class OpenaiClientConfig(BaseSettings):
    registration_name: str
    key: str
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
    mock_client_config: MockClientConfig
    ollama_client_config: OllamaClientConfig
    openai_client_config: OpenaiClientConfig


settings = Settings()
