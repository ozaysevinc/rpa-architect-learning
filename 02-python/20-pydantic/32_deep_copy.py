# ==========================================
# Python 87 - Deep Copy
# ==========================================

from pydantic import BaseModel


# ==========================================
# 1. Define Retry Configuration
# ==========================================

class RetryConfig(BaseModel):
    max_retries: int
    retry_delays: list[int]


# ==========================================
# 2. Define Bot Configuration
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    retry_config: RetryConfig


# ==========================================
# 3. Create Original Configuration
# ==========================================

original_config = BotConfig(
    bot_name="Finance Bot",
    retry_config=RetryConfig(
        max_retries=3,
        retry_delays=[5, 10, 15]
    )
)


# ==========================================
# 4. Create Shallow Copy
# ==========================================

shallow_config = original_config.model_copy()


# ==========================================
# 5. Create Deep Copy
# ==========================================

deep_config = original_config.model_copy(deep=True)


# ==========================================
# 6. Modify Nested Data
# ==========================================

shallow_config.retry_config.retry_delays.append(20)

deep_config.retry_config.retry_delays.append(30)


# ==========================================
# 7. Compare Configurations
# ==========================================

print("Original:", original_config.retry_config.retry_delays)
print("Shallow:", shallow_config.retry_config.retry_delays)
print("Deep:", deep_config.retry_config.retry_delays)