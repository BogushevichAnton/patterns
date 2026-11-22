"""Модуль сервиса."""

from patterns.src.common.protocol import UoW

from .repository import NoteRepository
from .schemas import Note, NoteRequest


class NoteService:

    def __init__(self, *, db_uow: UoW, repository: NoteRepository) -> None:
        self._db_uow = db_uow
        self._repository = repository

    async def get_notes(
        self,
        *,
        offset: int = 0,
        limit: int = 10,
        sort_by: str = "id",
        sort_order: str = "asc",
    ) -> list[Note]:
        notes_orm = await self._repository.get_notes(
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return [Note.model_validate(note) for note in notes_orm]

    async def create(self, *, note: NoteRequest) -> Note:
        async with self._db_uow:
            note_orm = await self._repository.create(
                title=note.title,
                description=note.description,
            )
            return Note.model_validate(note_orm)
