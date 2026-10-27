# ==========================================
# Python 88 - API Client with Dependency Injection
# ==========================================

from config import BotSettings


# ==========================================
# 1. Simulate API Connection
# ==========================================

def connect_to_api(settings: BotSettings):

    print("\n--- API CLIENT ---")

    print(f"Connecting to: {settings.api_url}")
    print(f"Connection timeout: {settings.timeout} seconds")

    print("API connection simulated successfully.")