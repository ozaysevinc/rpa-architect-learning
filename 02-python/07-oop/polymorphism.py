# ==========================================
# Python 72 - Polymorphism
# ==========================================


# ==========================================
# 1. Parent Class
# ==========================================

class RPABot:

    def __init__(self, bot_name):
        self.bot_name = bot_name

    def start(self):
        print(f"{self.bot_name} started.")


# ==========================================
# 2. Child Classes
# ==========================================

class FinanceBot(RPABot):

    def process(self):
        print("Connecting to finance system...")
        raise ConnectionError("Finance system connection failed.")


class HRBot(RPABot):

    def process(self):
        print("Processing employee record...")


class EmailBot(RPABot):

    def process(self):
        print("Sending email...")


# ==========================================
# 3. Create Bot Objects
# ==========================================

bots = [
    FinanceBot("FinanceBot"),
    HRBot("HRBot"),
    EmailBot("EmailBot")
]


# ==========================================
# 4. Run All Bots
# ==========================================

# for bot in bots:
#     bot.start()
#     bot.process()
#     print("--------------------")

# ==========================================
# 5. Reusable Bot Runner with Result
# ==========================================

def run_bot(bot):

    try:
        print(f"Running: {bot.bot_name}")

        bot.start()
        bot.process()

        print("Bot completed successfully.")
        return True

    except Exception as error:
        print(f"ERROR: {error}")
        return False

    finally:
        print("Bot execution finished.")
        print("--------------------")


# ==========================================
# 6. Test Bot Results
# ==========================================

finance_result = run_bot(FinanceBot("InvoiceBot"))
hr_result = run_bot(HRBot("EmployeeBot"))

print(f"Finance Bot Result: {finance_result}")
print(f"HR Bot Result: {hr_result}")