import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import main_app
from app.managers import ClientRegistry
from app.clients.mock_client import MockClient


@pytest_asyncio.fixture
async def async_client():
    client = AsyncClient(transport=ASGITransport(app=main_app), base_url="http://test")
    yield client
    await client.aclose()


@pytest.fixture
def generate_url():
    return "/generate/"


@pytest.mark.asyncio
async def test_generate_mock(async_client, generate_url):
    """Check the functionality of the mock client"""
    resp = await async_client.post(
        url=generate_url, json={"prompt": "hello", "client": "mock"}
    )
    assert resp.status_code == 200
    assert "Echo: hello" in resp.text


@pytest.mark.asyncio
async def test_generate_empty_prompt(async_client, generate_url):
    """Check behavior with an empty prompt"""
    resp = await async_client.post(
        url=generate_url, json={"prompt": "", "client": "mock"}
    )
    assert resp.status_code == 200
    assert "MOCK RESPONSE" in resp.text


@pytest.mark.asyncio
async def test_generate_unknown_client(async_client, generate_url):
    """Check behavior with an unknown client"""
    resp = await async_client.post(
        url=generate_url, json={"prompt": "hello", "client": "unknown"}
    )
    assert resp.status_code == 404
    assert "is not registered" in resp.json()["detail"]


@pytest.mark.asyncio
async def test_generate_openai_mock(async_client, generate_url):
    """OpenAIClient falls back to mock if API key is not set"""
    resp = await async_client.post(
        url=generate_url, json={"prompt": "test", "client": "openai"}
    )
    assert resp.status_code == 200
    assert "OPENAI-MOCK Echo: test" in resp.text


@pytest.mark.asyncio
async def test_registry_registration():
    """Check client registration"""

    class DummyClient(MockClient):
        async def generate(self, prompt: str) -> str:
            return "dummy"

    ClientRegistry.register("dummy")(DummyClient)
    client = ClientRegistry.create("dummy")
    result = await client.generate("test")
    assert result == "dummy"
