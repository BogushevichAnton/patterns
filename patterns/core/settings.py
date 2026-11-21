"""Глобальные настройки и переменные окружения проекта."""

import logging

from .config import (
    DatabaseConfig,
    FastAPIConfig,
    LoggerConfig,
    UvicornConfig,
)
from .utils import SingletonMeta, type_logger

logger1 = logging.getLogger()


class Settings(metaclass=SingletonMeta):
    def __init__(self) -> None:
        logger1.info("Инициализация настроек...")

        self.logger: LoggerConfig = LoggerConfig()

        logger1.debug("Инициализация настроек логирования...")
        type_logger.setup_logger(level=self.logger.level)
        logger1.debug("Инициализация настроек логирования завершена успешно!")

        self.db: DatabaseConfig = DatabaseConfig()
        self.fastapi: FastAPIConfig = FastAPIConfig()
        self.uvicorn: UvicornConfig = UvicornConfig()
        logger1.info("Инициализация настроек завершена успешно!")


settings = Settings()
