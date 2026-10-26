# ==========================================
# Python 87 - Model Validate JSON
# ==========================================

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Receive JSON Data
# ==========================================

json_data = """
{
    "bot_name": "Finance Bot",
    "timeout": 60,
    "max_retries": 3
}
"""


# ==========================================
# 3. Validate JSON with Pydantic
# ==========================================

config = BotConfig.model_validate_json(json_data)


# ==========================================
# 4. Display Configuration
# ==========================================

print(config.bot_name)
print(config.timeout)
print(config.max_retries)

print(type(config))