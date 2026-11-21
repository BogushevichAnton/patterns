"""Общие DI."""

from typing import Annotated

from fastapi import Depends

from patterns.core.db.di import UoWDep
from patterns.src.notes.service import NoteService


def get_note_service(db_uow: UoWDep) -> NoteService:
    return NoteService(db_uow=db_uow)


NoteServiceDep = Annotated[NoteService, Depends(get_note_service)]
