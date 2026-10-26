# ==========================================
# Python 87 - Pydantic ValidationError
# ==========================================

from pydantic import BaseModel, ValidationError


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    timeout: int
    max_retries: int


# ==========================================
# 2. Create Invalid Configuration
# ==========================================

try:
    config = BotConfig(
        bot_name="Finance Bot",
        timeout="abc",
        max_retries=3
    )

    print("Configuration created successfully.")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)