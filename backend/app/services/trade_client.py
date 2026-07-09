import time
import requests


class TradeClient:
    BASE_URL = "https://www.pathofexile.com/api/trade"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "PathOfJewel/0.1 contact: your-github-username"
        })

    def search(self, league: str, payload: dict):
        endpoint = f"search/{league}"
        return self._post(endpoint, payload)

    def fetch(self, item_ids: list[str], query_id: str):
        joined_ids = ",".join(item_ids)
        endpoint = f"fetch/{joined_ids}?query={query_id}"
        return self._get(endpoint)
    
    def get(self, endpoint: str):
        return self._get(endpoint)

    def _post(self, endpoint: str, payload: dict):
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.post(url, json=payload, timeout=20)
        return self._handle_response(response)

    def _get(self, endpoint: str):
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, timeout=20)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            time.sleep(retry_after)
            raise RuntimeError(f"Rate limited. Retry after {retry_after} seconds.")

        response.raise_for_status()
        return response.json()
    


trade_client = TradeClient()