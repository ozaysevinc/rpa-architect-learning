# ==========================================
# Python 60 - Refactored Retry Test
# ==========================================

from unittest.mock import patch
import requests

from api_retry_function import get_api_data

# ==========================================
# 1. Mock API Response
# ==========================================

def mock_get(url, timeout):
    response = requests.Response()
    response.status_code = 200
    response.url = url
    response._content = b'{"name": "Test User"}'
    return response


# ==========================================
# 2. Test Retry Function
# ==========================================

with patch("api_retry_function.requests.get", side_effect=mock_get):
    with patch("api_retry_function.time.sleep"):

        result = get_api_data(
            "https://example.com/api",
            max_retries=3
        )

        print(f"Result: {result}")