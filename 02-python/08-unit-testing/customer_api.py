# ==========================================
# Python 75 - Unit Testing
# Customer API
# ==========================================

import requests


# ==========================================
# 1. Get Customer
# ==========================================

def get_customer(customer_id):

    print("GET CUSTOMER FUNCTION IS RUNNING")

    url = f"https://api.example.com/customers/{customer_id}"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()