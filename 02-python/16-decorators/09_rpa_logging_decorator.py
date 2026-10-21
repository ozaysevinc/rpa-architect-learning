# ==========================================
# Python 83 - RPA Logging Decorator
# ==========================================

from functools import wraps


# ==========================================
# 1. Define Logging Decorator
# ==========================================

# ==========================================
# 1. Define Logging Decorator
# ==========================================

def add_logging(original_function):

    @wraps(original_function)
    def run_with_logging(*args, **kwargs):

        print(f"[START] {original_function.__name__}")

        try:
            result = original_function(*args, **kwargs)

            print(f"[SUCCESS] {original_function.__name__}")

            return result

        except Exception as error:

            print(f"[FAILED] {original_function.__name__}: {error}")

            raise

    return run_with_logging

# ==========================================
# 2. Define RPA Tasks
# ==========================================

@add_logging
def download_report(report_name):
    print(f"Downloading report: {report_name}")


@add_logging
def process_payment(customer, amount):
    print(f"Processing payment: {customer} - {amount} TL")
    return "PAYMENT_SUCCESS"


# ==========================================
# 3. Run RPA Bot
# ==========================================

download_report("Sales Report")

print()

payment_status = process_payment("Ahmet", 2500)

print(f"Payment status: {payment_status}")

# ==========================================
# 4. Test Failed Task
# ==========================================

@add_logging
def update_customer(customer_id):

    print(f"Updating customer: {customer_id}")

    raise ValueError("Customer not found")


try:
    update_customer(9999)

except ValueError:
    print("Bot detected the failed task.")