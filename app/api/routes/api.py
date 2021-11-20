
from fastapi import APIRouter

from app.api.routes import game_router

router = APIRouter()

router.include_router(game_router.router, tags=["games"], prefix="/game")