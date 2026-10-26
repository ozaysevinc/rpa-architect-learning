# ==========================================
# Python 87 - Assignment Validation
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
        validate_assignment=True
    )

    bot_name: str
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Valid Configuration
# ==========================================

config = BotConfig(
    bot_name="Finance Bot",
    timeout=30,
    max_retries=3
)

print(f"Initial timeout: {config.timeout}")


# ==========================================
# 3. Update Configuration
# ==========================================

try:
    config.timeout = -10

    print(f"Updated timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration update failed.")
    print(error)


# ==========================================
# 4. Check Current Configuration
# ==========================================

print(f"Current timeout: {config.timeout}")