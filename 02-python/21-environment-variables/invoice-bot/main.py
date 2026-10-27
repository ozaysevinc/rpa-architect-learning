# ==========================================
# Python 88 - Invoice Bot with DI
# ==========================================

from config import BotSettings, settings
from api_client import connect_to_api
from invoice_processor import process_invoices


# ==========================================
# 1. Main Bot Workflow
# ==========================================

def run_bot(bot_settings: BotSettings):

    print("================================")
    print(f"Starting: {bot_settings.bot_name}")
    print("================================")

    # Step 1: Connect to API
    connect_to_api(bot_settings)

    # Step 2: Process Invoices
    process_invoices(bot_settings)

    print("\n================================")
    print("Invoice Bot completed.")
    print("================================")


# ==========================================
# 2. Application Entry Point
# ==========================================

if __name__ == "__main__":
    run_bot(settings)