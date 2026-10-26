# ==========================================
# Python 87 - Model Serializer
# ==========================================

from typing import Any

from pydantic import BaseModel, Field, model_serializer


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    bot_name: str
    successful_tasks: int = Field(ge=0)
    failed_tasks: int = Field(ge=0)

    # ==========================================
    # 2. Customize Model Serialization
    # ==========================================

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:

        total_tasks = (
            self.successful_tasks + self.failed_tasks
        )

        return {
            "bot": self.bot_name,
            "total": total_tasks,
            "successful": self.successful_tasks,
            "failed": self.failed_tasks
        }


# ==========================================
# 3. Create Bot Execution
# ==========================================

execution = BotExecution(
    bot_name="Finance Bot",
    successful_tasks=90,
    failed_tasks=10
)


# ==========================================
# 4. Export Model
# ==========================================

print(execution.model_dump())