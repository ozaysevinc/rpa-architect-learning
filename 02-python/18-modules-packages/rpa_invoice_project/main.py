# ==========================================
# Python 85 - Finance Bot
# ==========================================


# ==========================================
# 1. Import Invoice Service
# ==========================================

from services.invoice_service import process_invoice


# ==========================================
# 2. Execute Finance Bot
# ==========================================

invoice_ids = [1001, 1002, 1003]

for invoice_id in invoice_ids:
    process_invoice(invoice_id)