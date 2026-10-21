# ==========================================
# Python 83 - functools.wraps
# ==========================================

from functools import wraps

# ==========================================
# 1. Define Decorator
# ==========================================

def add_logging(original_function):

    @wraps(original_function)
    def run_with_logging(*args, **kwargs):

        print("Task started.")

        result = original_function(*args, **kwargs)

        print("Task finished.")

        return result

    return run_with_logging


# ==========================================
# 2. Define RPA Task
# ==========================================

@add_logging
def process_order(order_id):
    print(f"Processing order: {order_id}")


# ==========================================
# 3. Check Function Name
# ==========================================

print(process_order.__name__)