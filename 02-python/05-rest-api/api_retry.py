# ==========================================
# Python 53 - API Retry Mechanism
# ==========================================

import requests
import time

# ==========================================
# 1. Configuration
# ==========================================

url = "https://jsonplaceholder.typicode.com/users/1"
max_retries = 3

# ==========================================
# 2. Retry Logic
# ==========================================

for attempt in range(1, max_retries + 1):

    print(f"Attempt {attempt}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        print("API request successful.")
        break

    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError):

        print("Connection failed.")

        if attempt < max_retries:
            print("Retrying in 2 seconds...")
            time.sleep(2)
        else:
            print("Maximum retry attempts reached.")