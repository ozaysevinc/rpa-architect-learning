# ==========================================
# Python 77 - Dataclass Default Values
# ==========================================

from dataclasses import dataclass


# ==========================================
# 1. Customer Model
# ==========================================

@dataclass
class Customer:
    customer_id: int
    name: str
    active: bool = True
    country: str = "Turkey"


# ==========================================
# 2. Create Customers
# ==========================================

customer_1 = Customer(101, "John")

customer_2 = Customer(102, "Michael", False)

customer_3 = Customer(103, "Sarah", country="Germany")




# ==========================================
# 3. Print Customers
# ==========================================

print(customer_1)
print(customer_2)
print(customer_3)