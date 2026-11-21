"""Модуль репозитория для работы c БД."""

from collections.abc import Sequence

from sqlalchemy import asc, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from .domain import Note


class NoteRepository:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_notes(
        self,
        offset: int = 0,
        limit: int = 10,
        sort_by: str = "id",
        sort_order: str = "asc",
    ) -> Sequence[Note]:
        sort_column = getattr(Note, sort_by, Note.id)
        order_func = asc if sort_order == "asc" else desc

        stmt = (
            select(Note).order_by(order_func(sort_column)).offset(offset).limit(limit)
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def create(self, **kwargs) -> Note:
        note_orm = Note(**kwargs)
        self._session.add(note_orm)
        await self._session.flush()
        return note_orm
