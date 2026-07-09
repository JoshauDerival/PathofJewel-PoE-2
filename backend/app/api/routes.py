from fastapi import APIRouter

from app.models.jewel import JewelRequest
from app.models.item_text import ItemTextRequest
from app.services.pricing_service import pricing_service
from app.services.item_parser_service import item_parser_service

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "PoE2 Jewel Pricer API"
    }


@router.post("/estimate")
def estimate(jewel: JewelRequest):
    return pricing_service.estimate_price(jewel)


@router.post("/parse-jewel")
def parse_jewel(request: ItemTextRequest):
    return item_parser_service.parse_jewel_text(request.item_text)


@router.post("/estimate-from-text")
def estimate_from_text(request: ItemTextRequest):
    jewel = item_parser_service.parse_jewel_text(request.item_text)
    estimate = pricing_service.estimate_price(jewel)

    return {
        "parsed_jewel": jewel,
        "estimate": estimate
    }