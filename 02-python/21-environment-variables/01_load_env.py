# ==========================================
# Python 88 - Load Environment Variables
# ==========================================

import os

from pathlib import Path
from dotenv import load_dotenv


# ==========================================
# 1. Load .env File
# ==========================================

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)


# ==========================================
# 2. Read Configuration
# ==========================================

bot_name = os.getenv("BOT_NAME")
api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")
timeout = int(os.getenv("TIMEOUT", "30"))


# ==========================================
# 3. Display Configuration
# ==========================================

print(f"Bot Name: {bot_name}")
print(f"API URL: {api_url}")
print(f"Timeout: {timeout}")

print(f"API Key Configured: {bool(api_key)}")