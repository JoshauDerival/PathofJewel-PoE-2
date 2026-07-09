from pydantic import BaseModel
from typing import List


class JewelAttribute(BaseModel):
    id: str = ""
    name: str
    value: float
    type: str = "explicit"


class JewelRequest(BaseModel):
    base_type: str
    item_level: int
    attributes: List[JewelAttribute]


class JewelResponse(BaseModel):
    estimated_price: str
    confidence: float


class PriceEstimate(BaseModel):
    price: float | None
    currency: str
    listing_count: int
    average: float | None = None
    median: float | None = None
    min: float | None = None
    max: float | None = None


class TradeMatch(BaseModel):
    price: float
    currency: str
    similarity: float


class EstimateAnalysis(BaseModel):
    matched_stats: list[dict]
    unmatched_stats: list[dict]


class EstimateDebug(BaseModel):
    trade_query: dict
    similarity_ready: bool


class EstimateResponse(BaseModel):
    estimate: PriceEstimate
    matches: list[TradeMatch]
    analysis: EstimateAnalysis
    debug: EstimateDebug
    note: str