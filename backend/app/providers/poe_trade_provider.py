from app.services.trade_client import trade_client


class PoeTradeProvider:

    def search(self, query: dict, league: str = "Dawn of the Hunt"):
        return trade_client.search(league, query)


poe_trade_provider = PoeTradeProvider()