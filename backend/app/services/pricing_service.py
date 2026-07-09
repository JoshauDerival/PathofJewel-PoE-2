from app.models.jewel import JewelRequest
from app.services.trade_service import trade_service


class PricingService:

    def estimate_price(self, jewel: JewelRequest):
        search = trade_service.build_search(jewel)

        score = 0

        for attribute in jewel.attributes:
            name = attribute.name.lower()
            value = attribute.value

            if "maximum life" in name:
                score += value * 3

            if "fire damage" in name:
                score += value * 1.5

            if "cold damage" in name:
                score += value * 1.5

            if "lightning damage" in name:
                score += value * 1.5

            if "critical" in name:
                score += value * 2

            if "resistance" in name:
                score += value * 1

        estimated_exalts = max(round(score / 10, 1), 1)

        confidence = min(round(score / 100, 2), 0.75)

        return {
            "estimated_price": f"{estimated_exalts} exalted",
            "confidence": confidence,
            "trade_query": search,
            "note": "This is a mock estimate. Real trade data will be added later."
        }


pricing_service = PricingService()