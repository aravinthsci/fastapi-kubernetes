from pydantic import BaseModel


class UpdateRequest(BaseModel):
    id: int
    name: str
    price: str
    rating: int
