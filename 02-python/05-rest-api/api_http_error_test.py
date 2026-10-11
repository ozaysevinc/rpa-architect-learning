# ==========================================
# Python 56 - HTTP Error Test
# ==========================================

import requests

# ==========================================
# 1. Simulate HTTP 503 Response
# ==========================================

response = requests.Response()
response.status_code = 503
response.url = "https://example.com/api"

# ==========================================
# 2. Check HTTP Error
# ==========================================

try:
    response.raise_for_status()

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")
    print(f"Status Code: {error.response.status_code}")