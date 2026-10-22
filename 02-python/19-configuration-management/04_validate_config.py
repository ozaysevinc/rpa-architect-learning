# ==========================================
# Python 86 - Configuration Validation Function
# ==========================================

import json
from pathlib import Path


# ==========================================
# 1. Load Configuration
# ==========================================

config_path = Path(__file__).parent / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)


# ==========================================
# 2. Validate Configuration
# ==========================================

def validate_config(config):

    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    if type(timeout) is not int or timeout <= 0:
        raise ValueError("Timeout must be a positive integer.")

    if type(max_retries) is not int or max_retries < 0:
        raise ValueError("Max retries must be a non-negative integer.")

    print("Configuration validation successful.")


# ==========================================
# 3. Start Finance Bot
# ==========================================

validate_config(config)

print("Finance Bot started.")