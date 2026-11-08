"""Реализация паттерна singleton."""

from typing import ClassVar, TypeVar

T = TypeVar("T")


class SingletonMeta(type):
    _instance: ClassVar[dict[type, object]] = {}

    def __call__(cls: type[T], *args, **kwargs) -> T:
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]
