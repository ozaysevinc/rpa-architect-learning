# ==========================================
# Python 82 - Iterable vs Iterator
# ==========================================


# ==========================================
# 1. Define Iterator
# ==========================================

class CustomerIterator:

    def __init__(self, customers):
        self.customers = customers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.customers):
            raise StopIteration

        customer = self.customers[self.index]
        self.index += 1

        return customer


# ==========================================
# 2. Define Iterable
# ==========================================

class CustomerCollection:

    def __init__(self, customers):
        self.customers = customers

    def __iter__(self):
        return CustomerIterator(self.customers)


# ==========================================
# 3. Create Collection
# ==========================================

customers = CustomerCollection([
    "Ahmet",
    "Mehmet",
    "Ayşe"
])


# ==========================================
# 4. First Loop
# ==========================================

print("First loop:")

for customer in customers:
    print(customer)


# ==========================================
# 5. Second Loop
# ==========================================

print("\nSecond loop:")

for customer in customers:
    print(customer)