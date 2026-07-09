from pydantic import BaseModel
from typing import List


class JewelAttribute(BaseModel):
    name: str
    value: float


class JewelRequest(BaseModel):
    base_type: str
    item_level: int
    attributes: List[JewelAttribute]


class JewelResponse(BaseModel):
    estimated_price: str
    confidence: float