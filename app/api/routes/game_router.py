from fastapi import APIRouter, status

from app.api.models.insert_request import InsertRequest
from app.api.models.update_request import UpdateRequest
from app.api.services.game_services import get_games, insert_game, update_games, delete_games

router = APIRouter()


@router.post("/insert/")
async def insert(body: InsertRequest):
    return await insert_game(body)


@router.get("/getGames/")
async def get():
    return await get_games()


@router.put("/updateGames/")
async def update(body: UpdateRequest):
    return await update_games(body)


@router.delete("/deleteGame/{gameID}")
async def update(gameID: int):
    return await delete_games(gameID)
