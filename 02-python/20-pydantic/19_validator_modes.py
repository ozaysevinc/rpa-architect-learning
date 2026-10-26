# ==========================================
# Python 87 - Validator Modes
# ==========================================

from typing import Any
from pydantic import BaseModel, field_validator


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    timeout: int

    # ==========================================
    # 2. Before Validator
    # ==========================================

    @field_validator("timeout", mode="before")
    @classmethod
    def clean_timeout(cls, value: Any) -> Any:

        print(f"Before Validator: {value}")

        if isinstance(value, str):
            return value.strip()

        return value

    # ==========================================
    # 3. After Validator
    # ==========================================

    @field_validator("timeout", mode="after")
    @classmethod
    def check_timeout(cls, value: int) -> int:

        print(f"After Validator: {value}")

        if value <= 0:
            raise ValueError("Timeout must be greater than 0")

        return value


# ==========================================
# 4. Create Configuration
# ==========================================

config = BotConfig(timeout=" 30 ")

print(f"Final Timeout: {config.timeout}")
print(f"Final Type: {type(config.timeout)}")