# ==========================================
# Python 83 - Flexible Decorator
# ==========================================


# ==========================================
# 1. Define Decorator
# ==========================================

def add_logging(original_function):

    def run_with_logging(*args, **kwargs):

        print("Task started.")

        result = original_function(*args, **kwargs)

        print("Task finished.")

        return result

    return run_with_logging


# ==========================================
# 2. Define RPA Tasks
# ==========================================

@add_logging
def process_order(order_id):
    print(f"Processing order: {order_id}")


@add_logging
def create_invoice(customer, amount):
    print(f"Creating invoice for {customer}: {amount} TL")


# ==========================================
# 3. Run Tasks
# ==========================================

process_order(1001)

print()

create_invoice(customer="Ahmet", amount=2500)