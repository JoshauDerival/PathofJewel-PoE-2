import json
from pathlib import Path


class MockTradeProvider:
    def __init__(self):
        path = Path(__file__).parent.parent / "data" / "mock_trade_listings.json"

        with open(path, "r", encoding="utf-8") as file:
            self.listings = json.load(file)

    def search(self, query: dict):
        return self.listings


mock_trade_provider = MockTradeProvider()