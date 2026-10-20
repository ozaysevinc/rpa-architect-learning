# ==========================================
# Python 80 - API Pagination Generator
# ==========================================


# ==========================================
# 1. Simulate API Request
# ==========================================

def fetch_customers(page: int):

    api_data = {
        1: [
            {"id": 101, "name": "Ahmet"},
            {"id": 102, "name": "Mehmet"}
        ],
        2: [
            {"id": 103, "name": "Ayşe"},
            {"id": 104, "name": "Zeynep"}
        ],
        3: [
            {"id": 105, "name": "Ali"}
        ]
    }

    print(f"Fetching API page: {page}")

    return api_data.get(page, [])


# ==========================================
# 2. Customer Generator
# ==========================================

def generate_customers():

    page = 1

    while True:

        customers = fetch_customers(page)

        if not customers:
            break

        for customer in customers:
            yield customer

        page += 1


# ==========================================
# 3. Process Customers
# ==========================================

print("Finance Bot started")

for customer in generate_customers():

    print(f"Processing customer: {customer['name']}")

print("Finance Bot completed")