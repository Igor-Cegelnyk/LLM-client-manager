import httpx

from app.clients.base import BaseLLMClient
from app.config import settings


class OpenAIClient(BaseLLMClient):

    @staticmethod
    def _build_payload(prompt: str) -> dict:
        return {
            "model": settings.openai_client_config.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 256,
        }

    @staticmethod
    def _build_headers(key: str) -> dict:
        return {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }

    async def generate(self, prompt: str) -> str:
        key = settings.openai_client_config.key
        if not key:
            return f"OPENAI-MOCK Echo: {prompt}"

        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                url=settings.openai_client_config.url,
                json=self._build_payload(prompt),
                headers=self._build_headers(key),
            )
            resp.raise_for_status()
            result = resp.json()
            return result["choices"][0]["message"]["content"].strip()
