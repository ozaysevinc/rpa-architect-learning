# ==========================================
# Python 77 - Dataclasses Mini Project
# ==========================================

from dataclasses import dataclass, field


# ==========================================
# 1. RPA Bot Model
# ==========================================

@dataclass
class RPABot:
    name: str
    retry_count: int = 3
    enabled: bool = True
    processed_customers: list[int] = field(default_factory=list)


# ==========================================
# 2. Process Customer
# ==========================================

def process_customer(bot: RPABot, customer_id: int) -> bool:

    if not bot.enabled:
        print(f"{bot.name} is disabled.")
        return False

    print(f"{bot.name} processing customer: {customer_id}")

    bot.processed_customers.append(customer_id)

    return True


# ==========================================
# 3. Create Bots
# ==========================================

finance_bot = RPABot(name="Finance Bot")
hr_bot = RPABot(name="HR Bot", enabled=True)


# ==========================================
# 4. Run Bots
# ==========================================

process_customer(finance_bot, 101)
process_customer(finance_bot, 102)
process_customer(hr_bot, 201)


# ==========================================
# 5. Print Results
# ==========================================

print(finance_bot)
print(hr_bot)