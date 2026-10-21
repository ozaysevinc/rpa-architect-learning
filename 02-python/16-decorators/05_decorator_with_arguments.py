# ==========================================
# Python 83 - Decorator with Arguments
# ==========================================


# ==========================================
# 1. Define Decorator
# ==========================================

def add_logging(original_function):

    def run_with_logging(order_id):

        print("Task started.")

        original_function(order_id)

        print("Task finished.")

    return run_with_logging


# ==========================================
# 2. Define RPA Task
# ==========================================

@add_logging
def process_order(order_id):
    print(f"Processing order: {order_id}")


# ==========================================
# 3. Run Task
# ==========================================

process_order(1001)