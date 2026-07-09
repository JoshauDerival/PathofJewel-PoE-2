class PoeTradeProvider:
    def search(self, query: dict):
        raise NotImplementedError(
            "Real PoE Trade integration has not been added yet."
        )


poe_trade_provider = PoeTradeProvider()