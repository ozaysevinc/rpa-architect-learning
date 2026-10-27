# ==========================================
# Python 88 - Pydantic Settings
# ==========================================

from pathlib import Path

from pydantic import Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================
# 1. Define Environment File Path
# ==========================================

env_path = Path(__file__).parent / ".env"


# ==========================================
# 2. Define Bot Settings
# ==========================================

class BotSettings(BaseSettings):

    bot_name: str = Field(min_length=2)
    api_url: HttpUrl
    api_key: SecretStr
    timeout: int = Field(gt=0)

    # ==========================================
    # 3. Configure Environment Loading
    # ==========================================

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
        extra="ignore"
    )


# ==========================================
# 4. Load and Validate Settings
# ==========================================

settings = BotSettings()


# ==========================================
# 5. Display Configuration
# ==========================================

print("Configuration loaded successfully.")

print(f"Bot Name: {settings.bot_name}")
print(f"API URL: {settings.api_url}")
print(f"Timeout: {settings.timeout}")
print(f"API Key: {settings.api_key}")