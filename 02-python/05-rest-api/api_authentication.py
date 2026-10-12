# ==========================================
# Python 61 - API Authentication
# ==========================================

import requests
from unittest.mock import patch

# ==========================================
# 1. API Configuration
# ==========================================

url = "https://example.com/api"
token = "wrong-token"

headers = {
    "Authorization": f"Bearer {token}"
}

# ==========================================
# 2. Mock API Authentication
# ==========================================

def mock_get(url, headers, timeout):

    authorization = headers.get("Authorization")

    response = requests.Response()

    if authorization == "Bearer test-token-123":
        response.status_code = 200
        response._content = b'{"message": "Access granted"}'
    else:
        response.status_code = 401
        response._content = b'{"message": "Unauthorized"}'

    return response

# ==========================================
# 3. Send API Request
# ==========================================

with patch("requests.get", side_effect=mock_get):

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")