# ==========================================
# Python 87 - Model Strict Validation
# ==========================================

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError
)


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):

    model_config = ConfigDict(strict=True)

    bot_name: str
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        timeout="30",
        max_retries=3
    )

    print("Configuration validated successfully.")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)