# ==========================================
# Python 73 - RPA Framework
# Bot Runner
# ==========================================


# ==========================================
# 1. Bot Runner Function
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
        bot.stop()
        print("Bot execution finished.")
        print("--------------------")

# ==========================================
# 2. Import Bots
# ==========================================

from finance_bot import FinanceBot
from hr_bot import HRBot


# ==========================================
# 3. Run Bots and Collect Results
# ==========================================

if __name__ == "__main__":

    bots = [
        FinanceBot("InvoiceBot"),
        HRBot("EmployeeBot")
    ]

    results = {}

    for bot in bots:
        result = run_bot(bot)
        results[bot.bot_name] = result

    print("=== BOT EXECUTION SUMMARY ===")

    for bot_name, result in results.items():
        print(f"{bot_name}: {result}")

    
    total_bots = len(results)

    successful_bots = sum(results.values())

    failed_bots = total_bots - successful_bots

    print("=== EXECUTION STATISTICS ===")
    print(f"Total Bots: {total_bots}")
    print(f"Successful Bots: {successful_bots}")
    print(f"Failed Bots: {failed_bots}")