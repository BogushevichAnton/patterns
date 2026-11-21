"""Доменные модели note."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from patterns.src.common import Base
from patterns.src.common.mixins.id import IdMixin


class Note(IdMixin, Base):
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100))
