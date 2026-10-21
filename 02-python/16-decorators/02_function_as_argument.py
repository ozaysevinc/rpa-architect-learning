# ==========================================
# Python 83 - Function as Argument
# ==========================================


# ==========================================
# 1. Define RPA Task
# ==========================================

def process_order():
    print("Order processed successfully.")


# ==========================================
# 2. Define Task Runner
# ==========================================

def run_task(task):
    print("Starting task...")

    task()

    print("Task completed.")


# ==========================================
# 3. Run Task
# ==========================================

run_task(process_order)