

from fastapi import HTTPException
from starlette import status

from app.clients.base import BaseLLMClient
from app.managers import ClientRegistry
from app.schemas.generate import GenerateRequest


async def get_client(
    req: GenerateRequest,
) -> BaseLLMClient:
    try:
        client = ClientRegistry.create(req.client)
        return client
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )