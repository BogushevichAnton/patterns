"""Версии API (v1, v2)."""

from fastapi import APIRouter

from .api_v1 import router_v1

api_router = APIRouter()
api_router.include_router(router_v1)
