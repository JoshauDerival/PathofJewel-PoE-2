from statistics import median


class PriceEstimatorService:

    def estimate(self, listings):
        if not listings:
            return {
                "price": None,
                "currency": "exalted",
                "listing_count": 0
            }

        prices = [listing["price"] for listing in listings]

        return {
            "price": median(prices),
            "currency": listings[0]["currency"],
            "listing_count": len(prices),
            "average": round(sum(prices) / len(prices), 2),
            "median": median(prices),
            "min": min(prices),
            "max": max(prices)
        }


price_estimator_service = PriceEstimatorService()