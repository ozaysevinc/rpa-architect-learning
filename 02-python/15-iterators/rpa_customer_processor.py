# ==========================================
# Python 82 - RPA Customer Processor
# ==========================================


# ==========================================
# 1. Define Customer Iterator
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
# 2. Define Customer Collection
# ==========================================

class CustomerCollection:

    def __init__(self, customers):
        self.customers = customers

    def __iter__(self):
        return CustomerIterator(self.customers)

# ==========================================
# 3. Define RPA Bot
# ==========================================

class CustomerBot:

    def process_customers(self, customers):

        for customer in customers:
            print(f"Processing customer: {customer}")

        print("All customers processed successfully.")

# ==========================================
# 4. Run RPA Bot
# ==========================================

customers = CustomerCollection([
    "Ahmet",
    "Mehmet",
    "Ayşe"
])

bot = CustomerBot()

bot.process_customers(customers)