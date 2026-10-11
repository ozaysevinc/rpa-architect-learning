# ==========================================
# Python 59 - Reusable API Retry Function
# ==========================================

import requests
import time

# ==========================================
# 1. Retry Delay Helper
# ==========================================

def wait_before_retry(attempt):
    wait_time = 2 ** (attempt - 1)
    print(f"Retrying in {wait_time} seconds...")
    time.sleep(wait_time)
# ==========================================
# 2. API Retry Function
# ==========================================


def get_api_data(url, max_retries=3):

    for attempt in range(1, max_retries + 1):

        print(f"Attempt {attempt}")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            print("API request successful.")
            return response.json()

        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):

            print("Connection failed.")

            if attempt < max_retries:
                wait_before_retry(attempt)
            else:
                print("Maximum retry attempts reached.")

        except requests.exceptions.HTTPError as error:

            status_code = error.response.status_code

            if status_code in [429, 500, 503]:
                print(f"Retryable HTTP error: {status_code}")

                if attempt < max_retries:
                    wait_before_retry(attempt)
                else:
                    print("Maximum retry attempts reached.")

            else:
                print(f"Non-retryable HTTP error: {status_code}")
                return None
    return None

# ==========================================
# 3. Test API Retry Function
# ==========================================

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users/99999"

    result = get_api_data(url, max_retries=3)

    if result is not None:
        print(f"User Name: {result['name']}")
    else:
        print("Failed to retrieve API data.")
