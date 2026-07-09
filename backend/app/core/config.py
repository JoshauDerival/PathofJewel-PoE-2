import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TRADE_PROVIDER: str = os.getenv("TRADE_PROVIDER", "mock")


settings = Settings()