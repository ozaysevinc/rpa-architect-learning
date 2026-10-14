# ==========================================
# Python 76 - RPA Type Hints
# ==========================================

from typing import TypedDict


# ==========================================
# 1. Customer Structure
# ==========================================

class Customer(TypedDict):
    id: int
    name: str
    email: str | None
    active: bool


# ==========================================
# 2. Process Customer
# ==========================================

def process_customer(customer: Customer) -> bool:

    if not customer["active"]:
        print(f"Skipping inactive customer: {customer['name']}")
        return False

    print(f"Processing customer: {customer['name']}")

    if customer["email"] is None:
        print("Customer has no email address.")

    return True


# ==========================================
# 3. Run
# ==========================================

customer: Customer = {
    "id": 101,
    "name": "John",
    "email": None,
    "active": False
}

result = process_customer(customer)

print(f"Process result: {result}")