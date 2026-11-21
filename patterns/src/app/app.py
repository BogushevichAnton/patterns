"""Модуль приложения fastapi."""

from fastapi import FastAPI

from patterns.core.settings import settings
from patterns.src.api import api_router

from .lifespan import lifespan
from .middleware import setup_cors


def create_app():
    fastapi_app = FastAPI(
        title=settings.fastapi.title,
        description=settings.fastapi.description,
        version=settings.fastapi.version,
        lifespan=lifespan,
    )

    setup_cors(fastapi_app)
    fastapi_app.include_router(api_router)
    return fastapi_app


app = create_app()
