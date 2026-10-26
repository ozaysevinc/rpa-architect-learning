# ==========================================
# Python 87 - Pydantic JSON Configuration
# ==========================================

import json
from pathlib import Path
from pydantic import BaseModel, Field


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    timeout: int = Field(default=30, gt=0)
    max_retries: int = Field(default=3, ge=0)


# ==========================================
# 2. Read JSON Configuration
# ==========================================

config_path = Path(__file__).parent / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    config_data = json.load(file)


# ==========================================
# 3. Validate with Pydantic
# ==========================================

config = BotConfig(**config_data)


# ==========================================
# 4. Start Finance Bot
# ==========================================

print(f"Bot Name: {config.bot_name}")
print(f"Timeout: {config.timeout}")
print(f"Max Retries: {config.max_retries}")

print("Finance Bot started.")