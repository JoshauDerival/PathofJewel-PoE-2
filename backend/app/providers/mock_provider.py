import json
from pathlib import Path


class MockTradeProvider:
    def __init__(self):
        path = Path(__file__).parent.parent / "data" / "mock_trade_listings.json"

        with open(path, "r", encoding="utf-8") as file:
            self.listings = json.load(file)

    def search(self, query: dict):
        results = []

        for index, listing in enumerate(self.listings):
            results.append(
                {
                    "id": f"mock-{index + 1}",
                    "price": {
                        "amount": listing["price"],
                        "currency": listing["currency"]
                    },
                    "seller": {
                        "name": "Mock Seller",
                        "online": True
                    },
                    "item_level": 82,
                    "attributes": listing["attributes"],
                    "similarity": 0.0
                }
            )

        return results


mock_trade_provider = MockTradeProvider()