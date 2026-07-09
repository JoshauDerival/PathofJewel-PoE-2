from app.models.jewel import JewelRequest
from app.services.trade_query_builder_service import trade_query_builder_service


class TradeService:

    def build_search(self, jewel: JewelRequest):
        return trade_query_builder_service.build_jewel_query(jewel)


trade_service = TradeService()