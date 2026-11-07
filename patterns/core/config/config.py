from pydantic import BaseModel
from .loader import PrivateLoader, PublicLoader
from pydantic_settings import SettingsConfigDict


class FastAPIConfig(PublicLoader):
    model_config = SettingsConfigDict(yaml_config_section="fastapi")
    title: str


class PublicDB(PublicLoader):
    model_config = SettingsConfigDict(yaml_config_section="db")
    host: str


class PrivateDB(PrivateLoader):
    model_config = SettingsConfigDict(
        env_prefix="DB__",
    )


class DatabaseConfig(BaseModel):
    private_config: PrivateDB
    public_config: PublicDB


class Settings(BaseModel):
    db: DatabaseConfig
    fastapi: FastAPIConfig


settings = Settings(
    db=DatabaseConfig(private_config=PrivateDB(), public_config=PublicDB()),
    fastapi=FastAPIConfig(),
)
