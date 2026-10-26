# ==========================================
# Python 87 - Combined Validators
# ==========================================

from typing import Literal, Self

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator,
    model_validator
)


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    environment: Literal["dev", "prod"]
    api_url: str
    timeout: int = Field(gt=0)

    # ==========================================
    # 2. Validate API URL
    # ==========================================

    @field_validator("api_url")
    @classmethod
    def validate_api_url(cls, value: str) -> str:

        if not value.startswith("https://"):
            raise ValueError("API URL must start with https://")

        return value

    # ==========================================
    # 3. Validate Production Timeout
    # ==========================================

    @model_validator(mode="after")
    def validate_production_timeout(self) -> Self:

        if self.environment == "prod" and self.timeout < 30:
            raise ValueError(
                "Production timeout must be at least 30 seconds"
            )

        return self


# ==========================================
# 4. Create Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        environment="prod",
        api_url="https://api.example.com",
        timeout=60
    )

    print("Configuration validated successfully.")
    print(f"Bot: {config.bot_name}")
    print(f"Environment: {config.environment}")
    print(f"API URL: {config.api_url}")
    print(f"Timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)