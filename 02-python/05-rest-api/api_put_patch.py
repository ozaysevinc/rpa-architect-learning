# ==========================================
# Python 64 - PUT and PATCH Requests
# ==========================================

import requests
from unittest.mock import patch

# ==========================================
# 1. Customer Data
# ==========================================

url = "https://example.com/customers/101"

customer = {
    "name": "Ali Demir",
    "email": "ali@new.com",
    "city": "Ankara"
}

# ==========================================
# 2. Mock PUT Request
# ==========================================

def mock_put(url, json, timeout):

    print(f"Received Data: {json}")

    response = requests.Response()
    response.status_code = 200
    response._content = b'{"message": "Customer updated successfully"}'

    return response

# ==========================================
# 3. Send PUT Request
# ==========================================

with patch("requests.put", side_effect=mock_put):

    response = requests.put(
        url,
        json=customer,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

# ==========================================
# 4. PATCH Data
# ==========================================

patch_data = {
    "city": "Izmir"
}

# ==========================================
# 5. Mock PATCH Request
# ==========================================

def mock_patch(url, json, timeout):

    print(f"PATCH Received Data: {json}")

    response = requests.Response()
    response.status_code = 200
    response._content = b'{"message": "Customer city updated"}'

    return response

# ==========================================
# 6. Send PATCH Request
# ==========================================

with patch("requests.patch", side_effect=mock_patch):

    response = requests.patch(
        url,
        json=patch_data,
        timeout=10
    )

    print(f"PATCH Status Code: {response.status_code}")
    print(f"PATCH Response: {response.json()}")