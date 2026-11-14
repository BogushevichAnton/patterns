"""Реализация паттерна Unit of Work."""

import logging
from typing import Any, Self

from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class DbUoW:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self) -> None:
        """Фиксирует транзакцию."""
        try:
            await self.session.commit()
        except Exception:
            logger.exception("Критическая ошибка при commit транзакции")
            await self.rollback()

    async def rollback(self) -> None:
        """Откатывает транзакцию."""
        try:
            await self.session.rollback()
        except Exception:
            logger.exception("Ошибка при rollback транзакции")
            raise

    async def __aenter__(self) -> Self:
        """Вход в контекстный менеджер."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        """
        Выход из контекстного менеджера.
        Если произошло исключение — откат, иначе — коммит.
        """
        if exc_type:
            logger.error(
                "Ошибка в транзакции: %s",
                exc_val,
                exc_info=(exc_type, exc_val, exc_tb),
            )
            await self.rollback()
        else:
            await self.commit()
