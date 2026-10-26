# ==========================================
# Python 87 - Execution Duration
# ==========================================

from datetime import datetime

from pydantic import BaseModel, model_validator


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
# 3. Simulate API Response
# ==========================================

api_response = {
    "bot_name": "Finance Bot",
    "started_at": "2026-10-26T09:00:00Z",
    "finished_at": "2026-10-26T09:05:30Z",
    "status": "completed"
}


# ==========================================
# 4. Validate API Response
# ==========================================

execution = BotExecution.model_validate(api_response)


# ==========================================
# 5. Calculate Execution Duration
# ==========================================

duration = execution.finished_at - execution.started_at

duration_seconds = duration.total_seconds()
duration_minutes = duration_seconds / 60


# ==========================================
# 6. Display Results
# ==========================================

print(f"Bot: {execution.bot_name}")
print(f"Status: {execution.status}")

print(f"Started At: {execution.started_at}")
print(f"Finished At: {execution.finished_at}")

print(f"Duration: {duration}")
print(f"Duration (seconds): {duration_seconds}")
print(f"Duration (minutes): {duration_minutes:.2f}")