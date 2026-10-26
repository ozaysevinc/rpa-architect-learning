# ==========================================
# Python 87 - Model Dump
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
# 2. Create Pydantic Model
# ==========================================

config = BotConfig(
    bot_name="Finance Bot",
    timeout=60
)


# ==========================================
# 3. Convert Model to Dictionary
# ==========================================

config_dict = config.model_dump()

print(config_dict)
print(type(config_dict))