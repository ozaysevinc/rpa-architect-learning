# ==========================================
# Python 87 - UUID Generation
# ==========================================

from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Bot Execution Model
# ==========================================

class BotExecution(BaseModel):
    execution_id: UUID = Field(default_factory=uuid4)
    bot_name: str
    status: str


# ==========================================
# 2. Create First Bot Execution
# ==========================================

execution_1 = BotExecution(
    bot_name="Finance Bot",
    status="completed"
)


# ==========================================
# 3. Create Second Bot Execution
# ==========================================

execution_2 = BotExecution(
    bot_name="Finance Bot",
    status="completed"
)


# ==========================================
# 4. Display Execution IDs
# ==========================================

print(f"First Execution ID: {execution_1.execution_id}")
print(f"Second Execution ID: {execution_2.execution_id}")


# ==========================================
# 5. Compare Execution IDs
# ==========================================

print(
    "IDs are different:",
    execution_1.execution_id != execution_2.execution_id
)