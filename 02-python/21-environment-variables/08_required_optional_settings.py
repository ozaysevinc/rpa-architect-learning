# ==========================================
# Python 88 - Required and Default Settings
# ==========================================

import logging
import sys

from pathlib import Path
from typing import Literal

from pydantic import Field, HttpUrl, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Project Paths
# ==========================================

BASE_DIR = Path(__file__).parent

ENV_FILE = BASE_DIR / ".env.invoice"


# ==========================================
# 2. Define Bot Settings
# ==========================================

class InvoiceBotSettings(BaseSettings):

    # Required settings
    bot_name: str = Field(min_length=2)
    api_url: HttpUrl

    # Settings with default values
    timeout: int = Field(default=30, gt=0)
    max_retries: int = Field(default=3, ge=0)

    log_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR"
    ] = "INFO"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore"
    )


# ==========================================
# 3. Define Bot Execution
# ==========================================

def run_bot(settings: InvoiceBotSettings):

    logging.basicConfig(
        level=settings.log_level,
        format="%(levelname)s | %(message)s"
    )

    logger = logging.getLogger(__name__)

    logger.info("Invoice Bot started.")

    print(f"Bot Name: {settings.bot_name}")
    print(f"API URL: {settings.api_url}")
    print(f"Timeout: {settings.timeout}")
    print(f"Max Retries: {settings.max_retries}")
    print(f"Log Level: {settings.log_level}")

    logger.info("Invoice Bot completed.")


# ==========================================
# 4. Load Configuration
# ==========================================

def main():

    try:
        settings = InvoiceBotSettings()

    except ValidationError as error:

        print("ERROR: Invalid configuration.")

        for detail in error.errors(
            include_input=False,
            include_context=False,
            include_url=False
        ):
            print(f"Field: {detail['loc']}")
            print(f"Message: {detail['msg']}")

        sys.exit(1)

    run_bot(settings)


# ==========================================
# 5. Application Entry Point
# ==========================================

if __name__ == "__main__":
    main()