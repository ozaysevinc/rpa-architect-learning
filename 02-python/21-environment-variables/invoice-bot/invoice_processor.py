# ==========================================
# Python 88 - Invoice Processor with DI
# ==========================================

from config import BotSettings


# ==========================================
# 1. Process Invoices
# ==========================================

def process_invoices(settings: BotSettings):

    print("\n--- INVOICE PROCESSOR ---")

    print(f"Processing with bot: {settings.bot_name}")
    print(f"Maximum retries: {settings.max_retries}")

    print("Invoice processing simulated successfully.")