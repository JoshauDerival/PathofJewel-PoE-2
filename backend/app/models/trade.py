from pydantic import BaseModel
from typing import List, Optional


class TradePrice(BaseModel):
    amount: float
    currency: str


class TradeSeller(BaseModel):
    name: Optional[str] = None
    online: bool = False


class TradeListing(BaseModel):
    id: str
    price: TradePrice
    seller: Optional[TradeSeller] = None
    item_level: Optional[int] = None
    attributes: List[str] = []
    similarity: float = 0.0


class TradeSearchResult(BaseModel):
    listings: List[TradeListing]
    total_results: int