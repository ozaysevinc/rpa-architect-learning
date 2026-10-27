# ==========================================
# Python 88 - Configuration Logging
# ==========================================

import logging
import os
import sys

from pathlib import Path

from pydantic import Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Project Paths
# ==========================================

BASE_DIR = Path(__file__).parent

LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

LOG_FILE = LOG_DIR / "bot.log"


# ==========================================
# 2. Configure Logging
# ==========================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


# ==========================================
# 3. Define Bot Settings
# ==========================================

class BotSettings(BaseSettings):
    bot_name: str = Field(min_length=2)
    api_url: HttpUrl
    timeout: int = Field(gt=0)

    model_config = SettingsConfigDict(
        extra="ignore"
    )


# ==========================================
# 4. Define Bot Execution
# ==========================================

def run_bot(settings: BotSettings):

    logger.info("Bot execution started.")

    print(f"Bot started: {settings.bot_name}")

    logger.info("Bot execution completed.")


# ==========================================
# 5. Load Configuration Safely
# ==========================================

def main():

    environment = os.getenv("APP_ENV", "dev").lower()

    logger.info(
        "Loading configuration for environment: %s",
        environment
    )

    if environment not in ("dev", "prod"):

        logger.error("Invalid environment: %s", environment)

        print("ERROR: Invalid environment.")

        sys.exit(1)

    env_file = BASE_DIR / f".env.{environment}"

    if not env_file.is_file():

        logger.error("Configuration file not found.")

        print("ERROR: Configuration file not found.")

        sys.exit(1)

    try:
        settings = BotSettings(_env_file=env_file)

    except ValidationError as error:

        logger.error("Configuration validation failed.")

        for detail in error.errors(
            include_input=False,
            include_url=False,
            include_context=False
        ):

            logger.error(
                "Field: %s | Error: %s",
                detail["loc"],
                detail["msg"]
            )

        print("ERROR: Configuration validation failed.")

        sys.exit(1)

    logger.info("Configuration validated successfully.")

    run_bot(settings)


# ==========================================
# 6. Application Entry Point
# ==========================================

if __name__ == "__main__":
    main()