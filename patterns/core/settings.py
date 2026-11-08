"""Глобальные настройки и переменные окружения проекта."""

import logging

from patterns.core.config import (
    DatabaseConfig,
    FastAPIConfig,
    LoggerConfig,
    UvicornConfig,
)
from patterns.utils import SingletonMeta, type_logger

logger1 = logging.getLogger()


class Settings(metaclass=SingletonMeta):
    logger1.info("Инициализация настроек...")

    logger: LoggerConfig = LoggerConfig()

    logger1.debug("Инициализация настроек логирования...")
    type_logger.setup_logger(level=logger.level)
    logger1.debug("Инициализация настроек логирования завершена успешно!")

    db: DatabaseConfig = DatabaseConfig()
    fastapi: FastAPIConfig = FastAPIConfig()
    uvicorn: UvicornConfig = UvicornConfig()
    logger1.info("Инициализация настроек завершена успешно!")


settings = Settings()
