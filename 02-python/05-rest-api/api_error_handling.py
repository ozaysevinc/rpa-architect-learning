# ==========================================
# Python 68 - API Error Handling
# ==========================================

import requests
from unittest.mock import patch
import time

# ==========================================
# 1. Mock API
# ==========================================

def mock_get(url, timeout):

    customer_id = int(url.split("/")[-1])

    if customer_id == 888:
        raise requests.exceptions.Timeout("ERP API timeout")

    if customer_id == 777:
        raise requests.exceptions.ConnectionError(
        "Cannot connect to ERP API"
    )       
    response = requests.Response()

    if customer_id == 101:
        response.status_code = 200
        response._content = b'{"name": "Ali Yilmaz"}'

    elif customer_id == 999:
        response.status_code = 404
        response._content = b'{"message": "Customer not found"}'

    else:
        response.status_code = 500
        response._content = b'{"message": "Internal server error"}'

    return response


# ==========================================
# 2. API Request Function with Error Handling
# ==========================================

def get_customer(customer_id):

    url = f"https://example.com/customers/{customer_id}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("SUCCESS: Customer found.")
            return response.json()

        elif response.status_code == 404:
            print("WARNING: Customer not found.")
            return None

        elif response.status_code == 500:
            print("ERROR: ERP server error.")
            return None

        else:
            print(f"ERROR: Unexpected status code {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("ERROR: ERP API request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to ERP API.")
        return None



# ==========================================
# 4. API Retry Function
# ==========================================

# ==========================================
# 4. API Retry with Exponential Backoff
# ==========================================

def get_customer_with_retry(customer_id, max_attempts=3):

    for attempt in range(1, max_attempts + 1):

        print(f"Attempt: {attempt}")

        try:
            url = f"https://example.com/customers/{customer_id}"

            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                print("SUCCESS: Customer found.")
                return response.json()

            if response.status_code == 404:
                print("WARNING: Customer not found.")
                return None

            if response.status_code == 500:
                print("ERROR: ERP server error.")

            else:
                print(f"ERROR: Unexpected status code {response.status_code}")
                return None

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError
        ):
            print("ERROR: Connection problem.")

        if attempt < max_attempts:

            wait_time = 2 ** (attempt - 1)

            print(f"Waiting {wait_time} seconds before retry...")

            time.sleep(wait_time)

    print("FAILED: Maximum retry attempts reached.")
    return None

# ==========================================
# 5. Mock API with Temporary Failures
# ==========================================

attempt_counter = 0


def mock_get_retry(url, timeout):

    global attempt_counter

    attempt_counter += 1

    if attempt_counter < 3:
        raise requests.exceptions.ConnectionError(
            "Temporary connection problem"
        )

    response = requests.Response()
    response.status_code = 200
    response._content = b'{"name": "Ali Yilmaz"}'

    return response


def mock_get_always_fails(url, timeout):

    raise requests.exceptions.ConnectionError(
        "ERP server is unavailable"
    )

# ==========================================
# 3. Test API Responses
# ==========================================

if __name__ == "__main__":
    print("\n--- Maximum Retry Test ---")

    with patch("requests.get", side_effect=mock_get_always_fails):

        result = get_customer_with_retry(101, max_attempts=3)

        print(f"Final Result: {result}")