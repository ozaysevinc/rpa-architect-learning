# ==========================================
# Python 84 - Outer Variables
# ==========================================


# ==========================================
# 1. Define Outer Function
# ==========================================

def run_bot():

    bot_name = "Finance Bot"

    def process_task():

        print(f"Running task for {bot_name}")

    process_task()


# ==========================================
# 2. Run Bot
# ==========================================

run_bot()