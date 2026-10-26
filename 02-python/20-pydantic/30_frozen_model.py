# ==========================================
# Python 87 - Frozen Model
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

    model_config = ConfigDict(
        frozen=True
    )

    bot_name: str
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Configuration
# ==========================================

config = BotConfig(
    bot_name="Finance Bot",
    timeout=30,
    max_retries=3
)

print(f"Initial timeout: {config.timeout}")


# ==========================================
# 3. Try to Update Configuration
# ==========================================

try:
    config.timeout = 60

    print(f"Updated timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration update failed.")
    print(error)


# ==========================================
# 4. Check Current Configuration
# ==========================================

print(f"Current timeout: {config.timeout}")