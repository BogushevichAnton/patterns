from patterns.utils import SingletonMeta
from patterns.core.config import DatabaseConfig, FastAPIConfig, UvicornConfig


class Settings(metaclass=SingletonMeta):
    db: DatabaseConfig = DatabaseConfig()
    fastapi: FastAPIConfig = FastAPIConfig()
    uvicorn: UvicornConfig = UvicornConfig()


settings = Settings()
