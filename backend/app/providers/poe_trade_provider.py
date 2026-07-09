from app.services.trade_client import trade_client


class PoeTradeProvider:

    def search(self, query: dict, league: str = "Dawn of the Hunt"):
        return trade_client.search(league, query)

    def fetch(self, item_ids: list[str], query_id: str):
        return trade_client.fetch(item_ids, query_id)


poe_trade_provider = PoeTradeProvider()