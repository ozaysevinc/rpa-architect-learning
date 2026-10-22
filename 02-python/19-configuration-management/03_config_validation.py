# ==========================================
# Python 86 - Configuration Validation
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
# 2. Validate Timeout
# ==========================================

timeout = config.get("timeout", 30)

if type(timeout) is not int or timeout <= 0:
    raise ValueError("Timeout must be a positive integer.")


# ==========================================
# 3. Start Bot
# ==========================================

print(f"Timeout: {timeout}")
print("Finance Bot started.")