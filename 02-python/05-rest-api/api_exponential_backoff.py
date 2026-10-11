# ==========================================
# Python 54 - Exponential Backoff
# ==========================================

import requests
import time

# ==========================================
# 1. Configuration
# ==========================================

url = "https://httpstat.us/503"
max_retries = 4

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
            wait_time = 2 ** (attempt - 1)
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print("Maximum retry attempts reached.")
    except requests.exceptions.HTTPError as error:

        status_code = error.response.status_code

        if status_code in [429, 500, 503]:

            print(f"Retryable HTTP error: {status_code}")

            if attempt < max_retries:
                wait_time = 2 ** (attempt - 1)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Maximum retry attempts reached.")

        else:
            print(f"Non-retryable HTTP error: {status_code}")
            break