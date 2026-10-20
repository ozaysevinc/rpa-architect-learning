# ==========================================
# Python 78 - Enums
# ==========================================

from enum import Enum


# ==========================================
# 1. Bot Status
# ==========================================

class BotStatus(Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCESS = "Success"
    FAILED = "Failed"


# ==========================================
# 2. Create Status
# ==========================================

status = BotStatus.RUNNING


# ==========================================
# 3. Print Status
# ==========================================

print(status)
print(status.name)
print(status.value)