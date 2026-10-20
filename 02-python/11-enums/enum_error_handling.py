# ==========================================
# Python 78 - Enum Error Handling
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
# 2. RPA Bot
# ==========================================

class RPABot:

    def __init__(self, name: str):
        self.name = name
        self.status = BotStatus.PENDING

    def run(self, customer_id: int):

        self.status = BotStatus.RUNNING

        try:
            print(f"Processing customer: {customer_id}")

            if customer_id < 0:
                raise ValueError("Invalid customer ID.")

            self.status = BotStatus.SUCCESS

        except ValueError as error:
            print(f"Error: {error}")
            self.status = BotStatus.FAILED

        finally:
            print(f"Final status: {self.status.value}")


# ==========================================
# 3. Run
# ==========================================

bot = RPABot("Finance Bot")

bot.run(101)
bot.run(-1)
bot.run(0)