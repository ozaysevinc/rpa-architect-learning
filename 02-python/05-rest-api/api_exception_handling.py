# ==========================================
# Python 52 - API Exception Handling
# ==========================================

import requests

# ==========================================
# 1. Send API Request
# ==========================================

url = "https://invalid.example"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("API request successful.")
    print(f"Status Code: {response.status_code}")

except requests.exceptions.Timeout:
    print("API request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to API.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")