"""Реализация паттерна singleton."""

from typing import Self


class SingletonMeta(type):
    _instance: dict[Self, Self] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]
