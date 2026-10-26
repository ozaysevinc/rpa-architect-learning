# ==========================================
# Python 87 - Strict Validation
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    timeout: int = Field(gt=0, strict=True)


# ==========================================
# 2. Create Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        timeout="30"
    )

    print("Configuration validated successfully.")
    print(f"Timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)