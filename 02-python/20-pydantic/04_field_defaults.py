# ==========================================
# Python 87 - Field Defaults
# ==========================================

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    timeout: int = Field(default=30, gt=0)
    max_retries: int = Field(default=3, ge=0)


# ==========================================
# 2. Create Configuration
# ==========================================

config = BotConfig(
    bot_name="Finance Bot"
)


# ==========================================
# 3. Display Configuration
# ==========================================

print(f"Bot Name: {config.bot_name}")
print(f"Timeout: {config.timeout}")
print(f"Max Retries: {config.max_retries}")