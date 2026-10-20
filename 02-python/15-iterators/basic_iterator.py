# ==========================================
# Python 82 - Basic Iterators
# ==========================================


# ==========================================
# 1. Create Customer List
# ==========================================

customers = ["Ahmet", "Mehmet", "Ayşe"]


# ==========================================
# 2. Create Iterator
# ==========================================

customer_iterator = iter(customers)

print("Iterator created")


# ==========================================
# 3. Get Customers
# ==========================================

print(next(customer_iterator))
print(next(customer_iterator))
print(next(customer_iterator))

customer_iterator = iter(customers)

print(next(customer_iterator))