# ==========================================
# Python 78 - Enum Mini RPA Project
# ==========================================

from enum import Enum
from dataclasses import dataclass


# ==========================================
# 1. Bot Status
# ==========================================

class BotStatus(Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCESS = "Success"
    FAILED = "Failed"


# ==========================================
# 2. Bot Model
# ==========================================

@dataclass
class RPABot:
    name: str
    status: BotStatus = BotStatus.PENDING
    processed_count: int = 0


# ==========================================
# 3. Process Customer
# ==========================================

def process_customer(bot: RPABot, customer_id: int) -> None:

    bot.status = BotStatus.RUNNING

    try:
        if customer_id <= 0:
            raise ValueError("Invalid customer ID.")

        print(f"Processing customer: {customer_id}")

        bot.processed_count += 1
        bot.status = BotStatus.SUCCESS

    except ValueError as error:
        print(f"Error: {error}")
        bot.status = BotStatus.FAILED

    finally:
        print(f"Bot status: {bot.status.value}")


# ==========================================
# 4. Run Bot
# ==========================================

bot = RPABot(name="Finance Bot")

process_customer(bot, 101)
process_customer(bot, 102)
process_customer(bot, -1)

print(bot)
process_customer(bot, 103)

print(bot)