from app.models.jewel import JewelRequest
from app.services.trade_service import trade_service
from app.services.stat_mapper_service import stat_mapper_service
from app.services.similarity_service import similarity_service
from app.services.trade_provider_service import trade_provider_service
from app.services.price_estimator_service import price_estimator_service

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

        target_ids = {
            attribute.id
            for attribute in jewel.attributes
            if attribute.id
        }

        results = []

        for listing in trade_provider_service.search(search):

            similarity = similarity_service.compare_listing(
                target_ids,
                listing
            )

            results.append(
                {
                "price": listing["price"],
                "currency": listing["currency"],
                "similarity": round(similarity, 2)
                }
            )

        results.sort(
            key=lambda x: (-x["similarity"], x["price"])
        )

        estimate = price_estimator_service.estimate(results[:5])

        return {
            "estimate": estimate,
            "matches": results[:5],
            "analysis": {
                "matched_stats": matched_stats,
                "unmatched_stats": unmatched_stats
            },
            "debug": {
                "trade_query": search,
                "similarity_ready": True
            },
            "note": "Estimate is based on mock comparable listings. Real trade listings will be added later."
        }


pricing_service = PricingService()