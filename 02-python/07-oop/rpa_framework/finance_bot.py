# ==========================================
# Python 73 - RPA Framework
# Finance Bot
# ==========================================

from base_bot import RPABot


# ==========================================
# 1. Finance Bot Class
# ==========================================

class FinanceBot(RPABot):

    def process(self):
        print(f"{self.bot_name} is processing invoices.")


# ==========================================
# 2. Test Finance Bot
# ==========================================

if __name__ == "__main__":

    finance_bot = FinanceBot("InvoiceBot")

    finance_bot.start()
    finance_bot.process()
    finance_bot.stop()