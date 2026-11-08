"""Класс конфигурации логгера."""

import logging


class Logger:
    def __init__(self) -> None:
        """Дефолтные настройки логгера."""
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        root_logger.addHandler(sh)

    def setup_logger(self, level: str) -> None:
        mapping = logging.getLevelNamesMapping()
        numeric_level = mapping.get(level.upper(), logging.INFO)

        root_logger = logging.getLogger()
        root_logger.setLevel(numeric_level)

        root_logger.handlers.clear()

        sh = logging.StreamHandler()
        sh.setLevel(numeric_level)

        root_logger.addHandler(sh)
        root_logger.propagate = False


type_logger = Logger()
