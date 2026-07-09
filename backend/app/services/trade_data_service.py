from app.services.trade_client import trade_client


class TradeDataService:

    def get_stats(self):
        return trade_client.get("data/stats")

    def search_stats(self, keyword: str):
        data = self.get_stats()
        keyword = keyword.lower()

        matches = []

        for group in data.get("result", []):
            group_label = group.get("label", "")

            for entry in group.get("entries", []):
                text = entry.get("text", "")
                stat_id = entry.get("id", "")

                if keyword in text.lower():
                    matches.append({
                        "group": group_label,
                        "id": stat_id,
                        "text": text
                    })

        return {
            "keyword": keyword,
            "count": len(matches),
            "matches": matches[:50]
        }


trade_data_service = TradeDataService()