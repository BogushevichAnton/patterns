from pydantic import BaseModel, SecretStr
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
    user: str
    password: SecretStr


class DatabaseConfig(BaseModel):
    private_config: PrivateDB = PrivateDB()
    public_config: PublicDB = PublicDB()


# class GlobalConfig(BaseModel):
#     db: DatabaseConfig
#     fastapi: FastAPIConfig


# settings = GlobalConfig(
#     db=DatabaseConfig(private_config=PrivateDB(), public_config=PublicDB()),
#     fastapi=FastAPIConfig(),
# )
