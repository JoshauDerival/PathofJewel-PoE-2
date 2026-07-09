from fastapi import APIRouter

from app.models.jewel import JewelRequest
from app.models.item_text import ItemTextRequest
from app.services.pricing_service import pricing_service
from app.services.item_parser_service import item_parser_service
from app.models.jewel import JewelRequest, EstimateResponse
from app.services.trade_data_service import trade_data_service


router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "PoE2 Jewel Pricer API"
    }


@router.post("/estimate", response_model=EstimateResponse)
def estimate(jewel: JewelRequest):
    return pricing_service.estimate_price(jewel)


@router.post("/parse-jewel")
def parse_jewel(request: ItemTextRequest):
    return item_parser_service.parse_jewel_text(request.item_text)


@router.post("/estimate-from-text", response_model=EstimateResponse)
def estimate_from_text(request: ItemTextRequest):
    jewel = item_parser_service.parse_jewel_text(request.item_text)
    return pricing_service.estimate_price(jewel)

@router.post("/build-trade-query")
def build_trade_query(jewel: JewelRequest):
    search = pricing_service.estimate_price(jewel)

    return {
        "trade_query": search["debug"]["trade_query"]
    }

@router.get("/trade-stats")
def trade_stats():
    return trade_data_service.get_stats()

@router.get("/trade-stats/search")
def search_trade_stats(keyword: str):
    return trade_data_service.search_stats(keyword)