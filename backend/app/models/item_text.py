from pydantic import BaseModel


class ItemTextRequest(BaseModel):
    item_text: str