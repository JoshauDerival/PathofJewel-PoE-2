import json
from pathlib import Path


class StatMapperService:
    def __init__(self):
        mapping_path = Path(__file__).parent.parent / "data" / "stat_mapping.json"

        with open(mapping_path, "r", encoding="utf-8") as file:
            self.stat_mapping = json.load(file)

    def map_stat(self, stat_name: str):
        stat_name_lower = stat_name.lower()

        for keyword, data in self.stat_mapping.items():
            if keyword in stat_name_lower:
                return {
                    "matched": True,
                    "keyword": keyword,
                    "trade_stat_id": data["id"],
                    "weight": data["weight"]
                }

        return {
            "matched": False,
            "keyword": None,
            "trade_stat_id": None,
            "weight": 1
        }


stat_mapper_service = StatMapperService()