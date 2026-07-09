from app.models.jewel import JewelRequest
from app.services.trade_service import trade_service
from app.services.stat_mapper_service import stat_mapper_service
from app.services.similarity_service import similarity_service

class PricingService:

    def estimate_price(self, jewel: JewelRequest):
        search = trade_service.build_search(jewel)

        total_score = 0
        matched_stats = []
        unmatched_stats = []

        for attribute in jewel.attributes:
            mapped_stat = stat_mapper_service.map_stat(attribute.name)

            stat_score = attribute.value * mapped_stat["weight"]
            total_score += stat_score

            stat_info = {
                "name": attribute.name,
                "value": attribute.value,
                "matched": mapped_stat["matched"],
                "trade_stat_id": mapped_stat["trade_stat_id"],
                "weight": mapped_stat["weight"],
                "score": round(stat_score, 2)
            }

            if mapped_stat["matched"]:
                matched_stats.append(stat_info)
            else:
                unmatched_stats.append(stat_info)

        estimated_exalts = max(round(total_score / 50, 1), 1)
        confidence = min(round(len(matched_stats) / max(len(jewel.attributes), 1), 2), 0.85)

        return {
            "estimated_price": f"{estimated_exalts} exalted",
            "confidence": confidence,
            "total_score": round(total_score, 2),
            "matched_stats": matched_stats,
            "unmatched_stats": unmatched_stats,
            "trade_query": search,
            "similarity_ready": True,
            "note": "Weighted mock estimate. Real trade listings will be added later."
        }


pricing_service = PricingService()