# ==========================================
# Python 76 - Optional Type Hints
# ==========================================

# ==========================================
# 1. Get Customer Phone
# ==========================================

def get_customer_phone(customer_id: int) -> str | None:

    if customer_id == 101:
        return "5551234567"

    return None


# ==========================================
# 2. Run
# ==========================================

phone_1 = get_customer_phone(101)
phone_2 = get_customer_phone(999)

print(f"Customer 101: {phone_1}")
print(f"Customer 999: {phone_2}")