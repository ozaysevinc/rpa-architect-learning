# ==========================================
# Python 87 - RPA Configuration Validator
# ==========================================

from typing import Literal, Self
from pydantic import BaseModel, Field, model_validator, ValidationError


# ==========================================
# 1. Define RPA Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    environment: Literal["dev", "prod"]
    timeout: int = Field(default=30, gt=0)
    api_key: str | None = None

    # ==========================================
    # 2. Validate Environment Requirements
    # ==========================================

    @model_validator(mode="after")
    def validate_production_config(self) -> Self:

        if self.environment == "prod" and not self.api_key:
            raise ValueError(
                "API key is required in production"
            )

        return self


# ==========================================
# 3. Create Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        environment="dev",
        timeout=30
    )

    print("Configuration validated successfully.")
    print(f"Bot: {config.bot_name}")
    print(f"Environment: {config.environment}")
    print(f"Timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)