# ==========================================
# Python 87 - Model Copy
# ==========================================

from pydantic import BaseModel, ConfigDict, Field


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):

    model_config = ConfigDict(frozen=True)

    bot_name: str
    timeout: int = Field(gt=0)
    max_retries: int = Field(ge=0)


# ==========================================
# 2. Create Original Configuration
# ==========================================

original_config = BotConfig(
    bot_name="Finance Bot",
    timeout=30,
    max_retries=3
)


# ==========================================
# 3. Create Updated Copy
# ==========================================

updated_config = original_config.model_copy(
    update={"timeout": 60}
)


# ==========================================
# 4. Compare Configurations
# ==========================================

print(f"Original timeout: {original_config.timeout}")
print(f"Updated timeout: {updated_config.timeout}")

print(f"Original retries: {original_config.max_retries}")
print(f"Updated retries: {updated_config.max_retries}")