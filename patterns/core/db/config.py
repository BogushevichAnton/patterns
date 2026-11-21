"""Модуль конфигурации ДБ engine."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from patterns.core.config import DatabaseConfig
from patterns.core.settings import settings
from patterns.core.utils import SingletonMeta


class DataBaseEngine(metaclass=SingletonMeta):
    def __init__(self, db_settings: DatabaseConfig):
        self._config = db_settings
        self.engine = create_async_engine(url=self._config.url)

    async def dispose(self) -> None:
        await self.engine.dispose()


class SessionFactory(metaclass=SingletonMeta):
    def __init__(self, engine: DataBaseEngine) -> None:
        self._session = async_sessionmaker(
            bind=engine.engine,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession,]:
        """
        Контекстный менеджер для получения сессии.

        Гарантирует закрытие сессии после выхода из контекста.
        """

        async with self._session() as session:
            yield session


session_factory = SessionFactory(engine=DataBaseEngine(settings.db))
