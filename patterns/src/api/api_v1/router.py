"""Первая версии API (v1)."""

from fastapi import APIRouter

from .note import notes

router_v1 = APIRouter(tags=["v1"])
router_v1.include_router(notes)
