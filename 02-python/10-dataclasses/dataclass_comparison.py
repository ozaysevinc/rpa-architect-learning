# ==========================================
# Python 77 - Dataclass Comparison
# ==========================================

from dataclasses import dataclass


# ==========================================
# 1. Customer Model
# ==========================================

@dataclass
class Customer:
    customer_id: int
    name: str


# ==========================================
# 2. Create Customers
# ==========================================

customer_1 = Customer(101, "John")
customer_2 = Customer(101, "John")
customer_3 = Customer(102, "Michael")


# ==========================================
# 3. Compare Customers
# ==========================================

print(customer_1 == customer_2)
print(customer_1 == customer_3)
print(customer_1 is customer_2)