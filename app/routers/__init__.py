__all__ = ["router"]

from fastapi import APIRouter

from .generate import router as generate



router = APIRouter()

router.include_router(generate)