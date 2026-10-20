# ==========================================
# Python 80 - Finance Payment Bot
# ==========================================


# ==========================================
# 1. Simulate API
# ==========================================

def fetch_payments(page: int) -> list[dict]:

    payments = {
        1: [
            {"customer_id": 101, "amount": 1500},
            {"customer_id": 102, "amount": 2500}
        ],
        2: [
            {"customer_id": 103, "amount": 0},
            {"customer_id": 104, "amount": 3500}
        ],
        3: [
            {"customer_id": 105, "amount": 5000}
        ]
    }

    print(f"Fetching payment page: {page}")

    return payments.get(page, [])


# ==========================================
# 2. Payment Generator
# ==========================================

def generate_payments():

    page = 1

    while True:

        payments = fetch_payments(page)

        if not payments:
            break

        for payment in payments:
            yield payment

        page += 1


# ==========================================
# 3. Process Payments
# ==========================================

success_count = 0
failed_count = 0

print("Finance Payment Bot started")

for payment in generate_payments():

    customer_id = payment["customer_id"]
    amount = payment["amount"]

    if amount > 0:
        print(f"Customer {customer_id}: SUCCESS")
        success_count += 1

    else:
        print(f"Customer {customer_id}: FAILED")
        failed_count += 1


# ==========================================
# 4. Print Summary
# ==========================================

print("\nFinance Payment Bot completed")

print(f"Successful payments: {success_count}")
print(f"Failed payments: {failed_count}")