from .base import BaseLLMClient

class MockClient(BaseLLMClient):
    async def generate(self, prompt: str) -> str:
        return f"MOCK RESPONSE Echo: {prompt}"