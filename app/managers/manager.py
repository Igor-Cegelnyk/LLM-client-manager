from typing import Callable, Dict, Type
from app.clients.base import BaseLLMClient


class ClientRegistry:
    _registry: Dict[str, Type[BaseLLMClient]] = {}

    @classmethod
    def register(cls, name: str) -> Callable[[Type[BaseLLMClient]], Type[BaseLLMClient]]:
        def _inner(client_cls: Type[BaseLLMClient]) -> Type[BaseLLMClient]:
            if name in cls._registry:
                raise KeyError(f"Client '{name}' already registered")
            cls._registry[name] = client_cls
            return client_cls

        return _inner

    @classmethod
    def create(cls, name: str) -> BaseLLMClient:
        client_cls = cls._registry.get(name)
        if not client_cls:
            raise KeyError(f"Client '{name}' is not registered")
        return client_cls()