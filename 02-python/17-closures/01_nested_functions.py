# ==========================================
# Python 84 - Nested Functions
# ==========================================


# ==========================================
# 1. Define Outer Function
# ==========================================

def run_bot():

    print("Bot started.")

    def process_task():
        print("Processing task...")

    process_task()

    print("Bot finished.")


# ==========================================
# 2. Run Bot
# ==========================================

run_bot()