# ==========================================
# Python 67 - API Client Refactoring
# ==========================================

import json
import requests
from unittest.mock import patch


# ==========================================
# 1. Mock Customer Database
# ==========================================

customers = {
    101: {"name": "Ali Yilmaz", "email": "ali@example.com"},
    102: {"name": "Ayse Demir", "email": "ayse@example.com"}
}


# ==========================================
# 2. Mock GET API
# ==========================================

def mock_get(url, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()

    if customer_id in customers:
        response.status_code = 200
        response._content = json.dumps(
            customers[customer_id]
        ).encode("utf-8")

    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response


# ==========================================
# 3. Reusable GET Function
# ==========================================

def get_customer(customer_id):

    url = f"https://example.com/customers/{customer_id}"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()

    return None



# ==========================================
# 5. Mock POST API
# ==========================================

def mock_post(url, json, timeout):

    response = requests.Response()

    if json.get("name") and json.get("email"):

        new_id = max(customers.keys()) + 1

        customers[new_id] = json.copy()

        response.status_code = 201
        response._content = (
            f'{{"id": {new_id}, "message": "Customer created"}}'
        ).encode("utf-8")

    else:
        response.status_code = 400
        response._content = b'{"message": "Name and email are required"}'

    return response

# ==========================================
# 6. Reusable POST Function
# ==========================================

def create_customer(name, email):

    url = "https://example.com/customers"

    customer_data = {
        "name": name,
        "email": email
    }

    response = requests.post(
        url,
        json=customer_data,
        timeout=10
    )

    if response.status_code == 201:
        return response.json()

    return None

# ==========================================
# 8. Mock PATCH API
# ==========================================

def mock_patch(url, json, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()

    if customer_id in customers:

        customers[customer_id].update(json)

        response.status_code = 200
        response._content = b'{"message": "Customer updated"}'

    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response

# ==========================================
# 9. Reusable PATCH Function
# ==========================================

def update_customer(customer_id, update_data):

    url = f"https://example.com/customers/{customer_id}"

    response = requests.patch(
        url,
        json=update_data,
        timeout=10
    )

    if response.status_code == 200:
        return response.json()

    return None

# ==========================================
# 11. Mock DELETE API
# ==========================================

def mock_delete(url, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()

    if customer_id in customers:

        del customers[customer_id]

        response.status_code = 204
        response._content = b""

    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response

# ==========================================
# 12. Reusable DELETE Function
# ==========================================

def delete_customer(customer_id):

    url = f"https://example.com/customers/{customer_id}"

    response = requests.delete(url, timeout=10)

    if response.status_code == 204:
        return True

    return False


# ==========================================
# 14. Run Tests Only When Executed Directly
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # Test GET Function
    # ==========================================

    with patch("requests.get", side_effect=mock_get):

        customer_101 = get_customer(101)
        customer_102 = get_customer(102)
        customer_999 = get_customer(999)

        print(f"Customer 101: {customer_101}")
        print(f"Customer 102: {customer_102}")
        print(f"Customer 999: {customer_999}")

    # ==========================================
    # Test POST Function
    # ==========================================

    with patch("requests.post", side_effect=mock_post):

        new_customer = create_customer(
            "Mehmet Kaya",
            "mehmet@example.com"
        )

        print(f"New Customer: {new_customer}")
        print(f"Customer 103: {customers.get(103)}")

    # ==========================================
    # Test PATCH Function
    # ==========================================

    with patch("requests.patch", side_effect=mock_patch):

        updated_customer = update_customer(
            103,
            {"email": "mehmet.yeni@example.com"}
        )

        print(f"Updated Customer: {updated_customer}")
        print(f"Customer 103: {customers.get(103)}")

    # ==========================================
    # Test DELETE Function
    # ==========================================

    with patch("requests.delete", side_effect=mock_delete):

        delete_result = delete_customer(103)

        print(f"Delete Result: {delete_result}")
        print(f"Customer 103 After DELETE: {customers.get(103)}")