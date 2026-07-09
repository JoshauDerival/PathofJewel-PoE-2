from app.core.config import settings
from app.providers.mock_provider import mock_trade_provider
from app.providers.poe_trade_provider import poe_trade_provider


class TradeProviderService:

    def search(self, query: dict):
        if settings.TRADE_PROVIDER == "mock":
            return mock_trade_provider.search(query)

        if settings.TRADE_PROVIDER == "poe":
            return poe_trade_provider.search(query)

        raise ValueError(f"Unknown trade provider: {settings.TRADE_PROVIDER}")


trade_provider_service = TradeProviderService()