# ==========================================
# Python 80 - Customer Generator
# ==========================================


# ==========================================
# 1. Generate Customers
# ==========================================

def generate_customers():

    customers = [
        {"id": 101, "name": "Ahmet"},
        {"id": 102, "name": "Mehmet"},
        {"id": 103, "name": "Ayşe"}
    ]

    for customer in customers:

        print(f"Fetching customer: {customer['id']}")

        yield customer


# =================================s=========
# 2. Process Customers
# ==========================================

customer_generator = generate_customers()

print("Finance Bot started")

for customer in customer_generator:

    print(f"Processing: {customer['name']}")

    print("Customer processed successfully.\n")

print("Finance Bot completed")