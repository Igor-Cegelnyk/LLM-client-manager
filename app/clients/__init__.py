from .mock_client import MockClient
from app.managers import ClientRegistry
from .ollama_client import OllamaClient

ClientRegistry.register("mock")(MockClient)
ClientRegistry.register("ollama")(OllamaClient)
