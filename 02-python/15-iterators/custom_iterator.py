# ==========================================
# Python 82 - Custom Iterator
# ==========================================


# ==========================================
# 1. Define Iterator Class
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
# 2. Create Iterator
# ==========================================

customers = ["Ahmet", "Mehmet", "Ayşe"]

customer_iterator = CustomerIterator(customers)


# ==========================================
# 3. Process Customers
# ==========================================

for customer in customer_iterator:

    print(f"Processing customer: {customer}")

print("Second loop:")

for customer in customer_iterator:
    print(customer)