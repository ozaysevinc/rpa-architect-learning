
# ==========================================
# Python 87 - Field Validation
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        timeout=30,
        max_retries=3
    )

    print("Configuration validated successfully.")
    print(f"Timeout: {config.timeout}")
    print(f"Max Retries: {config.max_retries}")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)