"""DTO схемы note."""

from pydantic import BaseModel, ConfigDict, Field


class BaseScnhema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class IdMixin:
    id: int = Field(..., description="Идентификатор")


class Note(IdMixin, BaseScnhema):
    title: str = Field(..., description="Наименование заметки")
    description: str = Field(..., description="Описание заметки")


class NoteRequest(BaseModel):
    title: str = Field(
        ..., description="Наименование заметки", min_length=5, max_length=50
    )
    description: str = Field(..., description="Описание заметки", max_length=100)
