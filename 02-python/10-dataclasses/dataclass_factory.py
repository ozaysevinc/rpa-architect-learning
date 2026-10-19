# ==========================================
# Python 77 - Dataclass Default Factory
# ==========================================

from dataclasses import dataclass, field


# ==========================================
# 1. RPA Bot Model
# ==========================================

@dataclass
class RPABot:
    name: str
    processed_customers: list[int] = field(default_factory=list)


# ==========================================
# 2. Create Bots
# ==========================================

finance_bot = RPABot("Finance Bot")
hr_bot = RPABot("HR Bot")


# ==========================================
# 3. Process Customers
# ==========================================

finance_bot.processed_customers.append(101)
finance_bot.processed_customers.append(102)

hr_bot.processed_customers.append(201)


# ==========================================
# 4. Print Results
# ==========================================

print(finance_bot)
print(hr_bot)