"""Точка входа в приложение."""

import uvicorn

from patterns.core import settings

if __name__ == "__main__":
    uvicorn.run(
        "patterns.core.app:fastapi_app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.debug,
        workers=settings.uvicorn.workers,
    )
