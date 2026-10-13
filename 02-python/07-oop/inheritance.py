# ==========================================
# Python 71 - Inheritance and super()
# ==========================================


# ==========================================
# 1. Parent Class
# ==========================================

class RPABot:

    def __init__(self, bot_name):
        self.bot_name = bot_name

    def start(self):
        print(f"{self.bot_name} started.")

    def stop(self):
        print(f"{self.bot_name} stopped.")


# ==========================================
# 2. Child Class
# ==========================================

class FinanceBot(RPABot):

    def __init__(self, bot_name, department):
        super().__init__(bot_name)
        self.department = department

    def start(self):
        print("Checking finance system connection...")
        super().start()

    def process_invoice(self):
        print(f"{self.bot_name} is processing invoices.")
        print(f"Department: {self.department}")


# ==========================================
# 3. Create Bot Object
# ==========================================

finance_bot = FinanceBot("InvoiceBot", "Accounting")


# ==========================================
# 4. Run Bot
# ==========================================

finance_bot.start()
finance_bot.process_invoice()
finance_bot.stop()

print("--------------------")
print(finance_bot.bot_name)
print(finance_bot.department)
print(finance_bot.start)