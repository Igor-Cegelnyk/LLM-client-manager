import httpx

from .base import BaseLLMClient
from app.config import settings


class OllamaClient(BaseLLMClient):

    @staticmethod
    def _build_payload(prompt: str) -> dict:
        return {
            "model": settings.ollama_client_config.model,
            "prompt": prompt,
            "max_tokens": 50,
        }

    @staticmethod
    def _parse_stream_line(line: str) -> dict | None:
        return httpx.Response(200, content=line.encode()).json()

    async def generate(self, prompt: str) -> str:
        full_response = ""

        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream(
                method="POST",
                url=settings.ollama_client_config.url,
                json=self._build_payload(prompt),
            ) as resp:
                resp.raise_for_status()
                async for line in resp.aiter_lines():
                    if line:
                        try:
                            chunk = self._parse_stream_line(line)
                            full_response += chunk.get("response", "")
                            if chunk.get("done", False):
                                break
                        except Exception:
                            continue

        return full_response
