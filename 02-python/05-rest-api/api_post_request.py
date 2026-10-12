# ==========================================
# Python 63 - POST Request
# ==========================================

import requests
from unittest.mock import patch

# ==========================================
# 1. Customer Data
# ==========================================

url = "https://example.com/customers"

customer = {
    "name": "Ali Yilmaz",
    "email": ""
}

# ==========================================
# 2. Mock POST Request
# ==========================================

def mock_post(url, json, timeout):

    response = requests.Response()

    if json.get("name") and json.get("email"):
        response.status_code = 201
        response._content = (
            '{"message": "Customer created successfully"}'
        ).encode("utf-8")
    else:
        response.status_code = 400
        response._content = (
            '{"message": "Name and email are required"}'
        ).encode("utf-8")

    return response

# ==========================================
# 3. Send POST Request
# ==========================================

with patch("requests.post", side_effect=mock_post):

    response = requests.post(
        url,
        json=customer,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")