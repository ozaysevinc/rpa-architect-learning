# ==========================================
# Python 51 - HTTP Status Code Handling
# ==========================================

import requests

# ==========================================
# 1. Send API Request
# ==========================================

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

# ==========================================
# 2. Check Status Code
# ==========================================

if response.status_code == 200:
    print("API request successful.")

elif response.status_code == 404:
    print("User not found.")

else:
    print(f"API request failed: {response.status_code}")