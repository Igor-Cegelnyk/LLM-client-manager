
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.clients.base import BaseLLMClient
from app.config import settings
from app.routers.dependencies import get_client
from app.schemas.generate import GenerateRequest

router = APIRouter(
    prefix=settings.api_prefix.generate,
    tags=["Public url"],
)


@router.post(
    "/",
    responses={503: {"description": "LLM provider error"}},
)
async def generate(
        req: GenerateRequest,
        client: BaseLLMClient = Depends(get_client)
) -> str:
    try:
        result = await client.generate(req.prompt)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"LLM provider error: {e}",
        )