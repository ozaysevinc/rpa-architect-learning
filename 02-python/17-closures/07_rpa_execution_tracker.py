# ==========================================
# Python 84 - RPA Execution Tracker
# ==========================================


# ==========================================
# 1. Define Bot Tracker
# ==========================================

def create_bot_tracker(bot_name):

    execution_count = 0

    def execute_bot():

        nonlocal execution_count

        execution_count += 1

        print(f"[START] {bot_name}")
        print(f"Execution number: {execution_count}")
        print(f"[SUCCESS] {bot_name}")

        return execution_count

    return execute_bot


# ==========================================
# 2. Create Bot Trackers
# ==========================================

finance_bot = create_bot_tracker("Finance Bot")
hr_bot = create_bot_tracker("HR Bot")


# ==========================================
# 3. Execute Bots
# ==========================================

finance_bot()
finance_bot()

print()

hr_bot()

print()

finance_bot()


sales_bot = create_bot_tracker("Sales Bot")

sales_bot()
sales_bot()