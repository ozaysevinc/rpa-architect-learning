# ==========================================
# Python 70 - Bot Configuration
# ==========================================


# ==========================================
# 1. Create RPA Bot Class
# ==========================================

class RPABot:

    def __init__(self, bot_name, max_customers):
        self.bot_name = bot_name
        self.max_customers = max_customers
        self.status = "Stopped"
        self.processed_count = 0

    def start(self):
        self.status = "Running"
        print(f"{self.bot_name} started.")

    def process(self):

        if self.status != "Running":
            print(f"ERROR: {self.bot_name} is not running.")
            return

        if self.processed_count >= self.max_customers:
            print(f"WARNING: {self.bot_name} reached customer limit.")
            return

        self.processed_count += 1
        print(f"{self.bot_name} processed a customer.")

    def stop(self):
        self.status = "Stopped"
        print(f"{self.bot_name} stopped.")

    def show_status(self):
        print(f"Bot Name: {self.bot_name}")
        print(f"Status: {self.status}")
        print(f"Processed Customers: {self.processed_count}")
        print(f"Customer Limit: {self.max_customers}")


# ==========================================
# 2. Create Bot Object
# ==========================================

bot = RPABot("FinanceBot", 3)


# ==========================================
# 3. Test Bot Workflow
# ==========================================

bot.start()

bot.process()
bot.process()
bot.process()
bot.process()

bot.stop()
bot.show_status()