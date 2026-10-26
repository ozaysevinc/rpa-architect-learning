# ==========================================
# Python 87 - Computed Execution Duration
# ==========================================

from datetime import datetime

from pydantic import (
    BaseModel,
    computed_field,
    model_validator
)


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    bot_name: str
    started_at: datetime
    finished_at: datetime
    status: str

    # ==========================================
    # 2. Validate Execution Times
    # ==========================================

    @model_validator(mode="after")
    def validate_execution_times(self):

        if self.finished_at < self.started_at:
            raise ValueError(
                "Finish time cannot be earlier than start time"
            )

        return self

    # ==========================================
    # 3. Calculate Duration Automatically
    # ==========================================

    @computed_field
    @property
    def duration_seconds(self) -> float:

        duration = self.finished_at - self.started_at

        return duration.total_seconds()


# ==========================================
# 4. Simulate API Response
# ==========================================

api_response = {
    "bot_name": "Finance Bot",
    "started_at": "2026-10-26T09:00:00Z",
    "finished_at": "2026-10-26T09:05:30Z",
    "status": "completed"
}


# ==========================================
# 5. Validate API Response
# ==========================================

execution = BotExecution.model_validate(api_response)


# ==========================================
# 6. Display Execution Information
# ==========================================

print(f"Bot: {execution.bot_name}")
print(f"Status: {execution.status}")

print(f"Duration: {execution.duration_seconds} seconds")


# ==========================================
# 7. Export Model as JSON
# ==========================================

print()
print(execution.model_dump_json(indent=2))