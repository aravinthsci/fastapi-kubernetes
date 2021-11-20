import json
from starlette.responses import JSONResponse
from fastapi import status
import pandas as pd

from app.api.db.database import get_db
from app.api.models.insert_request import InsertRequest
from app.api.models.update_request import UpdateRequest


async def insert_game(data_model: InsertRequest):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [data_model.name, data_model.price, data_model.rating])
    db.commit()
    return JSONResponse("New Game added to database", status_code=status.HTTP_200_OK)


async def get_games():
    conn = get_db()
    query = "SELECT id, name, price, rate FROM games"
    data_res = pd.read_sql(query, conn)
    return {"result": data_res.to_dict(orient='records')}


async def update_games(data_model: UpdateRequest):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [data_model.name, data_model.price, data_model.rating, data_model.id])
    db.commit()
    return JSONResponse("Successfully Updated Game in database", status_code=status.HTTP_200_OK)


async def delete_games(gameID):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [gameID])
    db.commit()
    return JSONResponse("Successfully Deleted Game in database", status_code=status.HTTP_200_OK)

