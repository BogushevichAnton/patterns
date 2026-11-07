import uvicorn
from fastapi import FastAPI
from patterns.core import settings

fastapi_app = FastAPI(
    title=settings.fastapi.title,
    description=settings.fastapi.description,
    version=settings.fastapi.version,
)

if __name__ == "__main__":
    uvicorn.run(
        "patterns.main:fastapi_app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.debug,
        workers=settings.uvicorn.workers,
    )
