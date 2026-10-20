# ==========================================
# Python 78 - Enum Conditions
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
# 2. Check Bot Status
# ==========================================

def check_bot_status(status: BotStatus) -> None:

    if status == BotStatus.SUCCESS:
        print("Bot completed successfully.")

    elif status == BotStatus.FAILED:
        print("Bot failed. Please check the logs.")

    else:
        print(f"Bot status: {status.value}")


# ==========================================
# 3. Run
# ==========================================

check_bot_status(BotStatus.SUCCESS)
check_bot_status(BotStatus.FAILED)
check_bot_status(BotStatus.RUNNING)
check_bot_status(BotStatus.PENDING)