# ==========================================
# Python 85 - Invoice Service
# ==========================================


# ==========================================
# 1. Import Logger
# ==========================================

from utils.logger import log_message


# ==========================================
# 2. Process Invoice
# ==========================================

def process_invoice(invoice_id):
    log_message(f"Invoice {invoice_id} started.")

    print(f"Processing invoice {invoice_id}...")

    log_message(f"Invoice {invoice_id} completed.")