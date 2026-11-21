from pydantic import BaseModel, Field, ConfigDict


class BaseScnhema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class IdMixin:
    id: int = Field(..., description="Идентификатор")


class Note(IdMixin, BaseScnhema):
    title: str = Field(..., description="Наименование заметки")
    description: str = Field(..., description="Описание заметки")
