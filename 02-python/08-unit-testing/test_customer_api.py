# ==========================================
# Python 75 - Unit Testing
# Mock API Test
# ==========================================

import unittest
from unittest.mock import patch

from customer_api import get_customer
from requests.exceptions import HTTPError


# ==========================================
# 1. Customer API Tests
# ==========================================

class TestCustomerAPI(unittest.TestCase):

    @patch("customer_api.requests.get")
    def test_get_customer(self, mock_get):

        mock_get.return_value.json.return_value = {
            "id": 101,
            "name": "John"
        }

        result = get_customer(101)

        self.assertEqual(result["id"], 101)
        self.assertEqual(result["name"], "John")

        mock_get.assert_called_once_with(
            "https://api.example.com/customers/101",
            timeout=10
        )
    # ==========================================
    # 2. Test API Error
    # ==========================================

    @patch("customer_api.requests.get")
    def test_get_customer_http_error(self, mock_get):

        mock_get.return_value.raise_for_status.side_effect = HTTPError(
            "404 Not Found"
        )

        with self.assertRaises(HTTPError):
            get_customer(999)


# ==========================================
# 2. Run Tests
# ==========================================

if __name__ == "__main__":
    unittest.main()