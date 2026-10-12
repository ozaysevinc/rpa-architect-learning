# ==========================================
# Python 67 - Customer RPA Bot
# ==========================================

from unittest.mock import patch

from api_client import (
    get_customer,
    mock_get
)


# ==========================================
# 1. Customer Lookup Workflow
# ==========================================

def run_customer_bot():

    customer_id = 101

    customer = get_customer(customer_id)

    if customer is not None:
        print(f"Customer found: {customer}")
        print("RPA workflow completed successfully.")
    else:
        print("Customer not found.")
        print("RPA workflow failed.")


# ==========================================
# 2. Run Bot with Mock API
# ==========================================

if __name__ == "__main__":

    with patch("requests.get", side_effect=mock_get):
        run_customer_bot()