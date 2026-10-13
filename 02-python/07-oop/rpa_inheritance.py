# ==========================================
# Python 71 - RPA Inheritance Project
# ==========================================


# ==========================================
# 1. Parent Class
# ==========================================

class RPABot:

    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.status = "Stopped"

    def start(self):
        self.status = "Running"
        print(f"{self.bot_name} started.")

    def stop(self):
        self.status = "Stopped"
        print(f"{self.bot_name} stopped.")


# ==========================================
# 2. Finance Bot
# ==========================================

class FinanceBot(RPABot):

    def process(self):
        if self.status != "Running":
            print("ERROR: FinanceBot is not running.")
            return

        print("Processing invoice...")


# ==========================================
# 3. HR Bot
# ==========================================

class HRBot(RPABot):

    def process(self):
        if self.status != "Running":
            print("ERROR: HRBot is not running.")
            return

        print("Processing employee record...")


# ==========================================
# 4. Run Bots
# ==========================================

finance_bot = FinanceBot("FinanceBot")
hr_bot = HRBot("HRBot")

finance_bot.start()
finance_bot.process()
finance_bot.stop()

print("--------------------")

hr_bot.start()
hr_bot.process()
hr_bot.stop()