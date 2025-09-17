from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    """Interface for LLM client"""

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        raise NotImplementedError