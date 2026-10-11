# ==========================================
# Python 57 - Mock API Retry Test
# ==========================================

import requests
import time
from unittest.mock import patch

# ==========================================
# 1. Mock API Response
# ==========================================

request_count = 0

def mock_get(url, timeout):
    global request_count

    request_count += 1

    response = requests.Response()
    response.url = url

    if request_count < 3:
        response.status_code = 503
    else:
        response.status_code = 200

    return response


# ==========================================
# 2. Retry Configuration
# ==========================================

url = "https://example.com/api"
max_retries = 4

# ==========================================
# 3. Mock API Request
# ==========================================

with patch("requests.get", side_effect=mock_get):

    for attempt in range(1, max_retries + 1):

        print(f"Attempt {attempt}")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            print("API request successful.")
            break

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