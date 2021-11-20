from pydantic import BaseModel


class InsertRequest(BaseModel):
    name: str
    price: str
    rating: int
