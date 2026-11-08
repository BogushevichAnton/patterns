"""Модуль приложения fastapi."""

from fastapi import FastAPI

from patterns.core import settings

from .lifespan import lifespan
from .middleware import setup_cors

fastapi_app = FastAPI(
    title=settings.fastapi.title,
    description=settings.fastapi.description,
    version=settings.fastapi.version,
    lifespan=lifespan,
)

setup_cors(fastapi_app)
