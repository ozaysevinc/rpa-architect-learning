# ==========================================
# Python 88 - Multiple Environments
# ==========================================

import os

from pathlib import Path

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Project Directory
# ==========================================

BASE_DIR = Path(__file__).parent


# ==========================================
# 2. Define Bot Settings
# ==========================================

class BotSettings(BaseSettings):
    bot_name: str
    api_url: HttpUrl
    timeout: int = Field(gt=0)

    model_config = SettingsConfigDict(
        extra="ignore"
    )


# ==========================================
# 3. Select Environment
# ==========================================

environment = os.getenv("APP_ENV", "dev").lower()

if environment not in ("dev", "prod"):
    raise ValueError(
        "APP_ENV must be 'dev' or 'prod'"
    )


# ==========================================
# 4. Select Environment File
# ==========================================

env_file = BASE_DIR / f".env.{environment}"


# ==========================================
# 5. Load and Validate Settings
# ==========================================

settings = BotSettings(_env_file=env_file)


# ==========================================
# 6. Display Configuration
# ==========================================

print(f"Environment: {environment}")
print(f"Bot Name: {settings.bot_name}")
print(f"API URL: {settings.api_url}")
print(f"Timeout: {settings.timeout}")