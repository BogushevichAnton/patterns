"""Эндпоинты API для управления заметками."""

from typing import Annotated, Literal

from fastapi import APIRouter, Query

from patterns.src.api.schemas import FilterBase, PaginationBase
from patterns.src.app.di import NoteServiceDep
from patterns.src.notes.schemas import Note, NoteRequest

router = APIRouter(prefix="/note")


@router.get("")
async def get_notes(
    service: NoteServiceDep,
    pagination_base: Annotated[PaginationBase, Query()],
    filter_base: Annotated[FilterBase[Literal["id", "title"]], Query()],
) -> list[Note]:
    return await service.get_notes(
        offset=pagination_base.offset,
        limit=pagination_base.limit,
        sort_by=filter_base.sort_by,
        sort_order=filter_base.sort_order,
    )


@router.post("")
async def create_note(
    note: NoteRequest,
    service: NoteServiceDep,
) -> Note:
    return await service.create(note=note)
