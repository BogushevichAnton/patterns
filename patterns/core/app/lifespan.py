"""Модуль lifespan."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Запуск приложения...")
    yield
    logger.info("Приложение остановлено!")
