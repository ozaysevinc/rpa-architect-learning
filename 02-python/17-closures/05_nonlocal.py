# ==========================================
# Python 84 - Nonlocal
# ==========================================


# ==========================================
# 1. Define Bot Counter
# ==========================================

def create_bot_counter():

    execution_count = 0

    def run_bot():

        nonlocal execution_count

        execution_count += 1

        print(f"Bot execution count: {execution_count}")

    return run_bot


# ==========================================
# 2. Create Bot
# ==========================================

bot = create_bot_counter()


# ==========================================
# 3. Run Bot
# ==========================================

bot()
bot()
bot()