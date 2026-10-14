# ==========================================
# Python 76 - TypedDict
# ==========================================

from typing import TypedDict


# ==========================================
# 1. Customer Structure
# ==========================================

class Customer(TypedDict):
    id: int
    name: str
    active: bool


# ==========================================
# 2. Get Customer
# ==========================================

def get_customer() -> Customer:

    customer: Customer = {
        "id": 11,
        "name": "John",
        "active": True
    }

    return customer


# ==========================================
# 3. Run
# ==========================================

result = get_customer()

print(result)
print(result["name"])