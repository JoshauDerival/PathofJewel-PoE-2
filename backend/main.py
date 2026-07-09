from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="PoE2 Jewel Pricer",
    description="A tool that estimates Path of Exile 2 jewel prices from item attributes.",
    version="0.1.0"
)


class JewelPriceRequest(BaseModel):
    jewel_name: str
    jewel_type: str
    attributes: List[str]


class JewelPriceResponse(BaseModel):
    estimated_price: str
    confidence: str
    message: str


@app.get("/")
def home():
    return {
        "message": "PoE2 Jewel Pricer API is running",
        "docs": "Go to /docs to test the API"
    }


@app.post("/estimate", response_model=JewelPriceResponse)
def estimate_price(jewel: JewelPriceRequest):
    return {
        "estimated_price": "Not available yet",
        "confidence": "low",
        "message": f"Received {jewel.jewel_name} with {len(jewel.attributes)} attributes."
    }