# ==========================================
# Python 87 - Combined Model Configuration
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
        strict=True,
        extra="forbid"
    )

    bot_name: str = Field(min_length=3)
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Simulate Configuration Data
# ==========================================

config_data = {
    "bot_name": "Finance Bot",
    "timeout": 30,
    "max_retries": 3,
    "debug_mode": True
}


# ==========================================
# 3. Validate Configuration
# ==========================================

try:
    config = BotConfig.model_validate(config_data)

    print("Configuration validated successfully.")
    print(config.model_dump())

except ValidationError as error:
    print("Configuration validation failed.")

    for detail in error.errors():
        print(f"Field: {detail['loc']}")
        print(f"Message: {detail['msg']}")