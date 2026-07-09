from app.providers.mock_provider import mock_trade_provider
from app.providers.poe_trade_provider import poe_trade_provider


class TradeProviderService:
    def __init__(self):
        self.mode = "mock"

    def search(self, query: dict):
        if self.mode == "mock":
            return mock_trade_provider.search(query)

        if self.mode == "poe":
            return poe_trade_provider.search(query)

        raise ValueError(f"Unknown trade provider mode: {self.mode}")


trade_provider_service = TradeProviderService()