# ==========================================
# 1. Process Customer
# ==========================================

def process_customer(customer_id: int, customer_name: str) -> bool:

    if not isinstance(customer_id, int):
        raise TypeError("Customer ID must be an integer.")

    if not isinstance(customer_name, str):
        raise TypeError("Customer name must be a string.")

    print(f"Processing customer: {customer_id} - {customer_name}")

    return True


# ==========================================
# 2. Run
# ==========================================

result = process_customer(101, 500)

print(f"Process result: {result}")