"""Базовые схемы для api."""

from typing import Literal

from pydantic import BaseModel, Field


class FilterBase[sortT](BaseModel):
    sort_by: sortT = Field(description="Поле для сортировки")
    sort_order: Literal["asc", "desc"] = Field(description="Направление сортировки")


class PaginationBase(BaseModel):
    offset: int = Field(
        default=0,
        ge=0,
        description="Количество записей, которое нужно пропустить от начала списка",
    )
    limit: int = Field(
        default=10,
        ge=1,
        le=30,
        description="Максимальное количество записей на странице",
    )
