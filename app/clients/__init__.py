from .mock_client import MockClient
from app.managers import ClientRegistry


ClientRegistry.register("mock")(MockClient)

