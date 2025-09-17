from .mock_client import MockClient
from app.managers import ClientRegistry
from .ollama_client import OllamaClient
from .openai_client import OpenAIClient
from app.config import settings

ClientRegistry.register(settings.mock_client_config.registration_name)(MockClient)
ClientRegistry.register(settings.ollama_client_config.registration_name)(OllamaClient)
ClientRegistry.register(settings.openai_client_config.registration_name)(OpenAIClient)
