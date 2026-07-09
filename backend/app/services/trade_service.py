from app.models.jewel import JewelRequest


class TradeService:

    def build_search(self, jewel: JewelRequest):

        return {
            "base_type": jewel.base_type,
            "item_level": jewel.item_level,
            "attributes": [
                {
                    "name": attribute.name,
                    "value": attribute.value
                }
                for attribute in jewel.attributes
            ]
        }


trade_service = TradeService()