# ==========================================
# Python 66 - Customer Management API
# ==========================================

import requests
import json
from unittest.mock import patch

# ==========================================
# 1. Mock Customer Database
# ==========================================

customers = {
    101: {
        "name": "Ali Yilmaz",
        "email": "ali@example.com"
    },
    102: {
        "name": "Ayse Demir",
        "email": "ayse@example.com"
    }
}

# ==========================================
# 2. Get Customer Function
# ==========================================

def get_customer(customer_id):

    if customer_id in customers:
        return customers[customer_id]

    return None

# ==========================================
# 3. Mock GET API
# ==========================================

def mock_get(url, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()
    response.url = url

    customer = get_customer(customer_id)

    if customer is not None:
        response.status_code = 200
        response._content = json.dumps(customer).encode("utf-8")
    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response

# ==========================================
# 4. Test GET API
# ==========================================

url = "https://example.com/customers/999"

with patch("requests.get", side_effect=mock_get):

    response = requests.get(url, timeout=10)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

# ==========================================
# 5. Mock POST API
# ==========================================

def mock_post(url, json, timeout):

    response = requests.Response()
    response.url = url

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
# 6. Test POST API
# ==========================================

new_customer = {
    "name": "Mehmet Kaya",
    "email": "mehmet@example.com"
}

with patch("requests.post", side_effect=mock_post):

    response = requests.post(
        "https://example.com/customers",
        json=new_customer,
        timeout=10
    )

    print(f"POST Status Code: {response.status_code}")
    print(f"POST Response: {response.json()}")

    print(f"Customer 103: {customers.get(103)}")

# ==========================================
# 7. Verify Created Customer with GET
# ==========================================

with patch("requests.get", side_effect=mock_get):

    response = requests.get(
        "https://example.com/customers/103",
        timeout=10
    )

    print(f"GET Status Code: {response.status_code}")
    print(f"GET Response: {response.json()}")

# ==========================================
# 8. Mock PATCH API
# ==========================================

def mock_patch(url, json, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()
    response.url = url

    if customer_id in customers:

        customers[customer_id].update(json)

        response.status_code = 200
        response._content = b'{"message": "Customer updated"}'

    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response

# ==========================================
# 9. Test PATCH API
# ==========================================

update_data = {
    "email": "mehmet.yeni@example.com"
}

with patch("requests.patch", side_effect=mock_patch):

    response = requests.patch(
        "https://example.com/customers/103",
        json=update_data,
        timeout=10
    )

    print(f"PATCH Status Code: {response.status_code}")
    print(f"PATCH Response: {response.json()}")

    print(f"Updated Customer: {customers.get(103)}")

# ==========================================
# 10. Mock DELETE API
# ==========================================

def mock_delete(url, timeout):

    customer_id = int(url.split("/")[-1])

    response = requests.Response()
    response.url = url

    if customer_id in customers:

        del customers[customer_id]

        response.status_code = 204
        response._content = b""

    else:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    return response

# ==========================================
# 11. Test DELETE API
# ==========================================

with patch("requests.delete", side_effect=mock_delete):

    response = requests.delete(
        "https://example.com/customers/103",
        timeout=10
    )

    print(f"DELETE Status Code: {response.status_code}")
    print(f"Customer 103 After DELETE: {customers.get(103)}")

# ==========================================
# 12. Verify Customer Deletion
# ==========================================

with patch("requests.get", side_effect=mock_get):

    response = requests.get(
        "https://example.com/customers/103",
        timeout=10
    )

    print(f"Verification Status Code: {response.status_code}")
    print(f"Verification Response: {response.json()}")

    if response.status_code == 404:
        print("SUCCESS: Customer deleted successfully.")
    else:
        print("ERROR: Customer still exists.")