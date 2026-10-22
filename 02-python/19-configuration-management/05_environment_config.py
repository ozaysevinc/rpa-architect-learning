# ==========================================
# Python 86 - Environment Configuration
# ==========================================

import json
from pathlib import Path


# ==========================================
# 1. Select Environment
# ==========================================

environment = "dev"
# environment = "prod"


# ==========================================
# 2. Locate Configuration File
# ==========================================

base_path = Path(__file__).parent

config_path = base_path / "configs" / f"{environment}.json"


# ==========================================
# 3. Load Configuration
# ==========================================

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)


# ==========================================
# 4. Display Bot Configuration
# ==========================================

print(f"Environment: {environment}")
print(f"Bot Name: {config['bot_name']}")
print(f"API URL: {config['api_url']}")
print(f"Max Retries: {config['max_retries']}")
print(f"Timeout: {config['timeout']}")