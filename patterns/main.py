import uvicorn
from fastapi import FastAPI
from patterns.core import settings

fastapi_app = FastAPI(
    title=settings.fastapi.title,
    description=settings.fastapi.description,
    version=settings.fastapi.version,
)

if __name__ == "__main__":
    uvicorn.run("patterns.main:fastapi_app", host="localhost", port=8080)
