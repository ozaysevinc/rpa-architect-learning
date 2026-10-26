# ==========================================
# Python 87 - Computed Field
# ==========================================

from pydantic import BaseModel, Field, computed_field


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    bot_name: str
    successful_tasks: int = Field(ge=0)
    failed_tasks: int = Field(ge=0)

    # ==========================================
    # 2. Calculate Total Tasks
    # ==========================================

    @computed_field
    @property
    def total_tasks(self) -> int:
        return self.successful_tasks + self.failed_tasks


# ==========================================
# 3. Create Bot Execution
# ==========================================

execution = BotExecution(
    bot_name="Finance Bot",
    successful_tasks=85,
    failed_tasks=15
)


# ==========================================
# 4. Display Results
# ==========================================

print(f"Bot: {execution.bot_name}")
print(f"Successful: {execution.successful_tasks}")
print(f"Failed: {execution.failed_tasks}")
print(f"Total: {execution.total_tasks}")


# ==========================================
# 5. Export Model
# ==========================================

print(execution.model_dump())