# ==========================================
# Python 87 - Basic Pydantic Model
# ==========================================

from pydantic import BaseModel


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    timeout: int
    max_retries: int


# ==========================================
# 2. Create Configuration
# ==========================================

config = BotConfig(
    bot_name="Finance Bot",
    timeout=30,
    max_retries=3
)


# ==========================================
# 3. Access Configuration Values
# ==========================================

print(config.bot_name)
print(config.timeout)
print(config.max_retries)