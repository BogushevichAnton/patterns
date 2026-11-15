"""Точка входа в приложение."""

import uvicorn

from patterns.core.settings import settings

print(settings)
if __name__ == "__main__":
    uvicorn.run(
        "patterns.src.app.app:app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.debug,
        workers=settings.uvicorn.workers,
    )
