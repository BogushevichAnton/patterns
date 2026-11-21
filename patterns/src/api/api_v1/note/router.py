"""Эндпоинты API для управления заметками."""

from fastapi import APIRouter

router = APIRouter(prefix="/note")


@router.get("")
async def get_notes() -> dict[str, bool]:
    return {"result": True}
