# ==========================================
# Python 87 - Field Serializer
# ==========================================

from pydantic import (
    BaseModel,
    Field,
    field_serializer
)


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    bot_name: str
    successful_tasks: int = Field(ge=0)
    failed_tasks: int = Field(ge=0)
    execution_time: float = Field(ge=0)

    # ==========================================
    # 2. Serialize Execution Time
    # ==========================================

    @field_serializer("execution_time")
    def serialize_execution_time(self, value: float) -> str:
        return f"{value:.2f} seconds"


# ==========================================
# 3. Create Bot Execution
# ==========================================

execution = BotExecution(
    bot_name="Finance Bot",
    successful_tasks=90,
    failed_tasks=10,
    execution_time=12.5678
)


# ==========================================
# 4. Access Original Value
# ==========================================

print(f"Original value: {execution.execution_time}")


# ==========================================
# 5. Export Model
# ==========================================

print(execution.model_dump())