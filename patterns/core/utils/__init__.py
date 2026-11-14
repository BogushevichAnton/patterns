"""Модуль utils.

Хранит:
    Singleton
    Logger
"""

__all__ = (
    "SingletonMeta",
    "type_logger",
)

from .logger import type_logger
from .singleton import SingletonMeta
