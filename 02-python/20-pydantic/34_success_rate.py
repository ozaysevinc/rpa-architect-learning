# ==========================================
# Python 87 - Computed Success Rate
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
    # 3. Calculate Success Rate
    # ==========================================

    @computed_field
    @property
    def success_rate(self) -> float:

        if self.total_tasks == 0:
            return 0.0

        rate = (
            self.successful_tasks / self.total_tasks
        ) * 100

        return round(rate, 2)


# ==========================================
# 4. Create Bot Execution
# ==========================================

execution = BotExecution(
    bot_name="Finance Bot",
    successful_tasks=80,
    failed_tasks=20
)


# ==========================================
# 5. Display Results
# ==========================================

print(f"Bot: {execution.bot_name}")
print(f"Total Tasks: {execution.total_tasks}")
print(f"Success Rate: {execution.success_rate}%")


# ==========================================
# 6. Export Model
# ==========================================

print(execution.model_dump())