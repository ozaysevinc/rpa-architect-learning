# ==========================================
# Python 84 - Multiple Closures
# ==========================================


# ==========================================
# 1. Define Bot Factory
# ==========================================

def create_bot(bot_name):

    def run_bot():
        print(f"Running: {bot_name}")

    return run_bot


# ==========================================
# 2. Create Bots
# ==========================================

finance_bot = create_bot("Finance Bot")

hr_bot = create_bot("HR Bot")

sales_bot = create_bot("Sales Bot")


# ==========================================
# 3. Run Bots
# ==========================================

finance_bot()

hr_bot()

sales_bot()