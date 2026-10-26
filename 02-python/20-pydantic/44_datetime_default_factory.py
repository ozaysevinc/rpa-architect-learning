# ==========================================
# Python 87 - Datetime Default Factory
# ==========================================

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    execution_id: UUID = Field(default_factory=uuid4)
    bot_name: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


# ==========================================
# 2. Create First Execution
# ==========================================

execution_1 = BotExecution(
    bot_name="Finance Bot"
)


# ==========================================
# 3. Create Second Execution
# ==========================================

execution_2 = BotExecution(
    bot_name="Invoice Bot"
)


# ==========================================
# 4. Display Execution Information
# ==========================================

print("First Execution:")
print(f"ID: {execution_1.execution_id}")
print(f"Created At: {execution_1.created_at}")

print()

print("Second Execution:")
print(f"ID: {execution_2.execution_id}")
print(f"Created At: {execution_2.created_at}")


# ==========================================
# 5. Export Model as JSON
# ==========================================

print()
print(execution_1.model_dump_json(indent=2))