from app.models.jewel import JewelRequest


class PricingService:

    def estimate_price(self, jewel: JewelRequest):

        return {
            "estimated_price": "Unknown",
            "confidence": 0.0
        }


pricing_service = PricingService()