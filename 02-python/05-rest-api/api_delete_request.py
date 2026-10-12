# ==========================================
# Python 65 - DELETE Request
# ==========================================

import requests
from unittest.mock import patch

# ==========================================
# 1. API Configuration
# ==========================================

url = "https://example.com/customers/999"

# ==========================================
# 2. Mock DELETE Request
# ==========================================

def mock_delete(url, timeout):

    print(f"Deleting Customer: {url}")

    response = requests.Response()

    if url.endswith("/101"):
        response.status_code = 204
    else:
        response.status_code = 404

    return response

# ==========================================
# 3. Send DELETE Request
# ==========================================

with patch("requests.delete", side_effect=mock_delete):

    response = requests.delete(
        url,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 204:
        print("Customer deleted successfully.")
    else:
        print("Delete operation failed.")