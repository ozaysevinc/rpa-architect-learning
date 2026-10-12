# ==========================================
# Python 69 - API Logging
# ==========================================

import logging
import requests
from unittest.mock import patch
from logging.handlers import RotatingFileHandler


# ==========================================
# 1. Configure Logger
# ==========================================

logger = logging.getLogger("CustomerAPIBot")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    "customer_api.log",
    maxBytes=1024 * 1024,
    backupCount=3,
    encoding="utf-8"
)

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# ==========================================
# 2. Mock API
# ==========================================

def mock_get(url, timeout):

    response = requests.Response()

    if url.endswith("/101"):
        response.status_code = 200
        response._content = b'{"name": "Ali Yilmaz"}'
    else:
        response.status_code = 404
        response._content = b'{"error": "Customer not found"}'

    return response


# ==========================================
# 3. Customer API Function
# ==========================================

def get_customer(customer_id):

    logger.info(f"Fetching customer {customer_id}")

    try:
        response = requests.get(
            f"https://example.com/customers/{customer_id}",
            timeout=10
        )

        logger.info(f"API status code: {response.status_code}")

        if response.status_code == 200:
            logger.info(f"Customer {customer_id} found.")
            return response.json()

        elif response.status_code == 404:
            logger.warning(f"Customer {customer_id} not found.")
            return None

        else:
            logger.error("Unexpected API response.")
            return None

    except requests.exceptions.RequestException as error:
        logger.error(f"API request failed: {error}")
        return None


# ==========================================
# 4. Run RPA Bot
# ==========================================

if __name__ == "__main__":

    logger.info("RPA bot started.")

    with patch("requests.get", side_effect=mock_get):

        get_customer(101)
        get_customer(999)

    logger.info("RPA bot finished.")