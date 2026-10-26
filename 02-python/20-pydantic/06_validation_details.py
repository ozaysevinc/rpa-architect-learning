# ==========================================
# Python 87 - Validation Error Details
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Invalid Configuration
# ==========================================

config_data = {
    "bot_name": "Finance Bot",
    "timeout": -10,
    "max_retries": 3
}


# ==========================================
# 3. Validate Configuration
# ==========================================

try:
    config = BotConfig(**config_data)
    print("Configuration validated successfully.")

except ValidationError as error:

    for detail in error.errors():
        print(f"Field: {detail['loc']}")
        print(f"Message: {detail['msg']}")
        print(f"Invalid Value: {detail.get('input')}")