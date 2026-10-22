# ==========================================
# Python 86 - RPA Configuration Manager
# ==========================================

import os
import json
from pathlib import Path


# ==========================================
# 1. Load Configuration
# ==========================================

def load_config():

    environment = os.getenv("BOT_ENV", "dev")

    if environment not in ["dev", "prod"]:
        raise ValueError("Invalid environment.")

    base_path = Path(__file__).parent

    config_path = base_path / "configs" / f"{environment}.json"

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config


# ==========================================
# 2. Validate Configuration
# ==========================================

def validate_config(config):

    timeout = config.get("timeout")
    max_retries = config.get("max_retries")

    if type(timeout) is not int or timeout <= 0:
        raise ValueError("Invalid timeout.")

    if type(max_retries) is not int or max_retries < 0:
        raise ValueError("Invalid max_retries.")

    print("Configuration validated.")