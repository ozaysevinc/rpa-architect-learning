# ==========================================
# Python 86 - Environment Variables
# ==========================================

import os
import json
from pathlib import Path


# ==========================================
# 1. Read Environment Variable
# ==========================================

environment = os.getenv("BOT_ENV", "dev")


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
# 4. Display Configuration
# ==========================================

print(f"Environment: {environment}")
print(f"Bot Name: {config['bot_name']}")
print(f"Timeout: {config['timeout']}")