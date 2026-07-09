class TradeQueryBuilderService:

    def build_jewel_query(self, jewel):
        filters = []

        for attribute in jewel.attributes:
            if attribute.id:
                filters.append(
                    {
                        "id": attribute.id,
                        "value": {
                            "min": attribute.value
                        },
                        "disabled": False
                    }
                )

        return {
            "query": {
                "status": {
                    "option": "online"
                },
                "type": jewel.base_type,
                "stats": [
                    {
                        "type": "and",
                        "filters": filters
                    }
                ]
            },
            "sort": {
                "price": "asc"
            }
        }


trade_query_builder_service = TradeQueryBuilderService()