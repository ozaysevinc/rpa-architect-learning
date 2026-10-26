# ==========================================
# Python 87 - Before Model Validator
# ==========================================

from typing import Any
from pydantic import BaseModel, Field, model_validator


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str = Field(min_length=3)
    environment: str
    timeout: int = Field(gt=0)

    # ==========================================
    # 2. Normalize Incoming Configuration
    # ==========================================

    @model_validator(mode="before")
    @classmethod
    def normalize_config(cls, data: Any) -> Any:

        if isinstance(data, dict):
            data = data.copy()

            if isinstance(data.get("environment"), str):
                data["environment"] = (
                    data["environment"].strip().lower()
                )

        return data


# ==========================================
# 3. Simulate Incoming Configuration
# ==========================================

config_data = {
    "bot_name": "Finance Bot",
    "environment": "  PROD  ",
    "timeout": 60
}


# ==========================================
# 4. Validate Configuration
# ==========================================

config = BotConfig.model_validate(config_data)

print(f"Bot: {config.bot_name}")
print(f"Environment: {config.environment}")
print(f"Timeout: {config.timeout}")