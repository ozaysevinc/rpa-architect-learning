# ==========================================
# Python 84 - Independent Closures
# ==========================================


# ==========================================
# 1. Define Bot Counter
# ==========================================

def create_bot_counter(bot_name):

    execution_count = 0

    def run_bot():

        nonlocal execution_count

        execution_count += 1

        print(f"{bot_name}: {execution_count}")

    return run_bot


# ==========================================
# 2. Create Independent Bots
# ==========================================

finance_bot = create_bot_counter("Finance Bot")

hr_bot = create_bot_counter("HR Bot")


# ==========================================
# 3. Run Bots
# ==========================================

finance_bot()
finance_bot()

hr_bot()

finance_bot()

hr_bot()