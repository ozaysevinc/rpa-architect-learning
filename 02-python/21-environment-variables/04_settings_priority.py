# ==========================================
# Python 88 - Settings Priority
# ==========================================

import os

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Environment File
# ==========================================

env_path = Path(__file__).parent / ".env"


# ==========================================
# 2. Define Bot Settings
# ==========================================

class BotSettings(BaseSettings):
    bot_name: str = "Default Bot"
    timeout: int = Field(default=30, gt=0)

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
        extra="ignore"
    )


# ==========================================
# 3. Load Settings From .env
# ==========================================

settings = BotSettings()

print("Settings from .env:")
print(f"Bot Name: {settings.bot_name}")
print(f"Timeout: {settings.timeout}")


# ==========================================
# 4. Override With Environment Variable
# ==========================================

os.environ["TIMEOUT"] = "60"

updated_settings = BotSettings()

print()
print("Settings after environment override:")
print(f"Bot Name: {updated_settings.bot_name}")
print(f"Timeout: {updated_settings.timeout}")


# ==========================================
# 5. Clean Up Environment Variable
# ==========================================

os.environ.pop("TIMEOUT", None)