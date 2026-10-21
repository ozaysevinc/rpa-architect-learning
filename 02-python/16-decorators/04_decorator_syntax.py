# ==========================================
# Python 83 - Decorator Syntax
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

@add_logging
def process_order():
    print("Processing order...")


# ==========================================
# 3. Run Task
# ==========================================

process_order()