# ==========================================
# Python 62 - Environment Variables
# ==========================================

import os
import requests
from unittest.mock import patch

# ==========================================
# 1. Read Environment Variable
# ==========================================

api_token = os.getenv("API_TOKEN")

if not api_token:
    print("API token not found.")
    raise SystemExit(1)

# ==========================================
# 2. Prepare API Request
# ==========================================

url = "https://example.com/api"

headers = {
    "Authorization": f"Bearer {api_token}"
}

# ==========================================
# 3. Mock API Authentication
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
# 4. Send API Request
# ==========================================

with patch("requests.get", side_effect=mock_get):

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")