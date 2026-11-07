from pydantic import BaseModel, SecretStr, computed_field
from .loader import PrivateLoader, PublicLoader
from pydantic_settings import SettingsConfigDict
from importlib.metadata import version, PackageNotFoundError


class FastAPIConfig(PublicLoader):
    model_config = SettingsConfigDict(yaml_config_section="fastapi")
    title: str
    description: str

    @computed_field
    @property
    def version(self) -> str:
        """Автоматически вычисляет версию на основе pyproject.toml.

        ограничение по title. title fastapi == pyproject.toml ["name"]
        """
        try:
            return version(self.title)
        except PackageNotFoundError:
            raise


class UvicornConfig(PublicLoader):
    model_config = SettingsConfigDict(yaml_config_section="uvicorn")
    host: str
    port: int
    debug: bool
    workers: int


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
