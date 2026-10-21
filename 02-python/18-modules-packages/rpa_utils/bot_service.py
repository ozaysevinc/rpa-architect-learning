# ==========================================
# Python 85 - Absolute and Relative Imports
# ==========================================


# ==========================================
# 1. Relative Import
# ==========================================

from .logger import log_message


# ==========================================
# 2. Bot Service
# ==========================================

def execute_finance_bot():
    log_message("Finance Bot started.")

    print("Processing invoices...")

    log_message("Finance Bot completed.")