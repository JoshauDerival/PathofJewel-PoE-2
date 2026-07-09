from fastapi import APIRouter

from app.models.jewel import JewelRequest
from app.services.pricing_service import pricing_service

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "PoE2 Jewel Pricer API"
    }


@router.post("/estimate")
def estimate(jewel: JewelRequest):

    return pricing_service.estimate_price(jewel)