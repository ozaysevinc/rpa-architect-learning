# ==========================================
# Python 86 - Basic Configuration
# ==========================================

import json
from pathlib import Path


# ==========================================
# 1. Locate Configuration File
# ==========================================

config_path = Path(__file__).parent / "config.json"


# ==========================================
# 2. Read Configuration
# ==========================================

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)


# ==========================================
# 3. Access Configuration Values
# ==========================================

bot_name = config["bot_name"]
max_retries = config["max_retries"]
timeout = config["timeout"]

print(f"Bot Name: {bot_name}")
print(f"Max Retries: {max_retries}")
print(f"Timeout: {timeout}")