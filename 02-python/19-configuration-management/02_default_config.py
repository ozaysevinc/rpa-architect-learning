# ==========================================
# Python 86 - Default Configuration
# ==========================================

import json
from pathlib import Path


# ==========================================
# 1. Read Configuration
# ==========================================

config_path = Path(__file__).parent / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)


# ==========================================
# 2. Read Values with Defaults
# ==========================================

bot_name = config.get("bot_name", "Unknown Bot")
max_retries = config.get("max_retries", 3)
timeout = config.get("timeout", 30)

print(f"Bot Name: {bot_name}")
print(f"Max Retries: {max_retries}")
print(f"Timeout: {timeout}")