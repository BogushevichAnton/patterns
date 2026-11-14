"""FastAPI зависимости для работы c БД и Unit of Work."""

from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .config import session_factory
from .uow import DbUoW


async def get_session() -> AsyncGenerator[AsyncSession,]:
    """
    Dependency для получения сессии (для чтения).
    """
    async with session_factory.get_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


async def get_uow(
    session: SessionDep,
) -> AsyncGenerator[DbUoW,]:
    """Dependency для получения Unit of Work (для записи)."""
    async with DbUoW(session) as uow:
        yield uow


UoWDep = Annotated[DbUoW, Depends(get_uow)]
