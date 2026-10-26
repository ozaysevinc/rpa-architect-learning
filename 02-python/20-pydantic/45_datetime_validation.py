# ==========================================
# Python 87 - Datetime Validation
# ==========================================

from datetime import datetime

from pydantic import BaseModel, ValidationError


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    bot_name: str
    started_at: datetime
    status: str


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "bot_name": "Finance Bot",
    "started_at": "2026-10-26T14:30:00Z",
    "status": "completed"
}


# ==========================================
# 3. Validate API Response
# ==========================================

try:
    execution = BotExecution.model_validate(api_response)

    print("Execution validated successfully.")

    print(f"Bot: {execution.bot_name}")
    print(f"Started At: {execution.started_at}")
    print(f"Status: {execution.status}")

    # ==========================================
    # 4. Check Data Type
    # ==========================================

    print(f"Started At Type: {type(execution.started_at)}")

except ValidationError as error:
    print("Execution validation failed.")
    print(error)