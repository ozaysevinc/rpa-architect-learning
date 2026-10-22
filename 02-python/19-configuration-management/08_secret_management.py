# ==========================================
# Python 86 - Secret Management
# ==========================================

import os


# ==========================================
# 1. Read API Key
# ==========================================

api_key = os.getenv("FINANCE_API_KEY")


# ==========================================
# 2. Validate API Key
# ==========================================

if not api_key:
    raise ValueError("FINANCE_API_KEY is not configured.")


# ==========================================
# 3. Start Finance Bot
# ==========================================

print("API key loaded successfully.")

print("Finance Bot started.")