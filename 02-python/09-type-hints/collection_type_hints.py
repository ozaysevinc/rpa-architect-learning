# ==========================================
# Python 76 - Collection Type Hints
# ==========================================

# ==========================================
# 1. Process Customer IDs
# ==========================================

def process_customers(customer_ids: list[int]) -> int:

    for customer_id in customer_ids:
        print(f"Processing customer: {customer_id}")

    return len(customer_ids)


# ==========================================
# 2. Run
# ==========================================

customers = [101, 102, 103]

total = process_customers(customers)

print(f"Total processed: {total}")