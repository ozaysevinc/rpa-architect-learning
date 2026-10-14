# ==========================================
# Python 76 - Dictionary Type Hints
# ==========================================

# ==========================================
# 1. Get Customer
# ==========================================

def get_customer() -> dict[str, str]:

    customer = {
        "name": "John",
        "email": "john@example.com"
    }

    return customer


# ==========================================
# 2. Run
# ==========================================

result = get_customer()

print(result)
print(result["name"])