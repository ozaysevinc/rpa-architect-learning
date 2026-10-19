# ==========================================
# Python 77 - Dataclasses
# ==========================================

from dataclasses import dataclass


# ==========================================
# 1. Customer Model
# ==========================================

@dataclass
class Customer:
    customer_id: int
    name: str
    active: bool


# ==========================================
# 2. Create Customer
# ==========================================

customer = Customer(
    customer_id=101,
    name="John",
    active=True
)


# ==========================================
# 3. Print Customer
# ==========================================

print(customer)
print(customer.name)
print(customer.active)