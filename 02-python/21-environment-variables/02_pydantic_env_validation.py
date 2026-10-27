# ==========================================
# Python 88 - Pydantic Environment Validation
# ==========================================

import os

from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field, HttpUrl, SecretStr, ValidationError


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=2)
    api_url: HttpUrl
    api_key: SecretStr
    timeout: int = Field(gt=0)


# ==========================================
# 2. Load Environment Variables
# ==========================================

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)


# ==========================================
# 3. Prepare Configuration Data
# ==========================================

config_data = {
    "bot_name": os.getenv("BOT_NAME"),
    "api_url": os.getenv("API_URL"),
    "api_key": os.getenv("API_KEY"),
    "timeout": os.getenv("TIMEOUT")
}


# ==========================================
# 4. Validate Configuration
# ==========================================

try:
    config = BotConfig.model_validate(config_data)

    print("Configuration validated successfully.")

    print(f"Bot Name: {config.bot_name}")
    print(f"API URL: {config.api_url}")
    print(f"Timeout: {config.timeout}")

    print(f"API Key: {config.api_key}")

except ValidationError as error:

    print("Configuration validation failed.")

    for detail in error.errors():
        print(f"Field: {detail['loc']}")
        print(f"Message: {detail['msg']}")