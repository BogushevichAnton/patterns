from patterns.utils import SingletonMeta
from patterns.core.config import DatabaseConfig, FastAPIConfig


class Settings(metaclass=SingletonMeta):
    db: DatabaseConfig = DatabaseConfig()
    fastapi: FastAPIConfig = FastAPIConfig()


settings = Settings()
