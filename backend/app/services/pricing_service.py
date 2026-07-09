from app.models.jewel import JewelRequest
from app.services.trade_service import trade_service


class PricingService:

    def estimate_price(self, jewel: JewelRequest):

        search = trade_service.build_search(jewel)

        return {
            "estimated_price": "Unknown",
            "confidence": 0.0,
            "trade_query": search
        }


pricing_service = PricingService()