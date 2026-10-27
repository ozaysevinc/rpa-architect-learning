# ==========================================
# Python 88 - Safe Configuration Loading
# ==========================================

import os
import sys

from pathlib import Path

from pydantic import Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Project Directory
# ==========================================

BASE_DIR = Path(__file__).parent


# ==========================================
# 2. Define Bot Settings
# ==========================================

class BotSettings(BaseSettings):
    bot_name: str = Field(min_length=2)
    api_url: HttpUrl
    timeout: int = Field(gt=0)

    model_config = SettingsConfigDict(
        extra="ignore"
    )


# ==========================================
# 3. Define Bot Execution
# ==========================================

def run_bot(settings: BotSettings):

    print("Bot started successfully.")

    print(f"Bot Name: {settings.bot_name}")
    print(f"API URL: {settings.api_url}")
    print(f"Timeout: {settings.timeout}")

    print("Bot execution completed.")


# ==========================================
# 4. Load Configuration Safely
# ==========================================

def main():

    environment = os.getenv("APP_ENV", "dev").lower()

    if environment not in ("dev", "prod"):
        print("ERROR: Invalid environment.")
        sys.exit(1)

    env_file = BASE_DIR / f".env.{environment}"

    if not env_file.is_file():
        print(f"ERROR: Configuration file not found: {env_file}")
        sys.exit(1)

    try:
        settings = BotSettings(_env_file=env_file)

    except ValidationError as error:

        print("ERROR: Configuration validation failed.")

        for detail in error.errors():
            print(f"Field: {detail['loc']}")
            print(f"Message: {detail['msg']}")

        sys.exit(1)

    # ==========================================
    # 5. Start Bot Only If Config Is Valid
    # ==========================================

    run_bot(settings)


# ==========================================
# 6. Application Entry Point
# ==========================================

if __name__ == "__main__":
    main()