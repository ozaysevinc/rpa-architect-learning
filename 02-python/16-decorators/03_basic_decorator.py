# ==========================================
# Python 83 - Basic Decorator
# ==========================================


# ==========================================
# 1. Define Decorator
# ==========================================

def add_logging(original_function):

    def run_with_logging():

        print("Task started.")

        original_function()

        print("Task finished.")

    return run_with_logging


# ==========================================
# 2. Define RPA Task
# ==========================================

def process_order():
    print("Processing order...")


# ==========================================
# 3. Apply Decorator
# ==========================================

process_order = add_logging(process_order)


# ==========================================
# 4. Run Task
# ==========================================

process_order()