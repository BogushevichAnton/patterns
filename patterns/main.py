import uvicorn
from fastapi import FastAPI

fastapi_app = FastAPI(title="patterns of programming")

if __name__ == "__main__":
    uvicorn.run("patterns.main:fastapi_app", host="localhost", port=8080)
