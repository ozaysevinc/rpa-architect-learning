# ==========================================
# Python 88 - Centralized Configuration
# ==========================================

from pathlib import Path
from typing import Literal

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Project Paths
# ==========================================

BASE_DIR = Path(__file__).parent


# ==========================================
# 2. Define Application Settings
# ==========================================

class BotSettings(BaseSettings):

    bot_name: str = Field(min_length=2)
    api_url: HttpUrl

    timeout: int = Field(default=30, gt=0)
    max_retries: int = Field(default=3, ge=0)

    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR"
    ] = "INFO"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# ==========================================
# 3. Create Settings Instance
# ==========================================

settings = BotSettings()