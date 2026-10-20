# ==========================================
# Python 78 - Bot Status Management
# ==========================================

from enum import Enum


# ==========================================
# 1. Bot Status Enum
# ==========================================

class BotStatus(Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCESS = "Success"
    FAILED = "Failed"


# ==========================================
# 2. RPA Bot
# ==========================================

class RPABot:

    def __init__(self, name: str):
        self.name = name
        self.status = BotStatus.PENDING

    def run(self):
        self.status = BotStatus.RUNNING
        print(f"{self.name}: {self.status.value}")

        print("Processing customers...")

        self.status = BotStatus.FAILED
        print(f"{self.name}: {self.status.value}")


# ==========================================
# 3. Run Bot
# ==========================================

bot = RPABot("Finance Bot")

print(f"Initial status: {bot.status.value}")

bot.run()

print(f"Final status: {bot.status.value}")