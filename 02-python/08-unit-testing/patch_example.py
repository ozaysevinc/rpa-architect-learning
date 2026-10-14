# ==========================================
# Python 75 - Patch Example
# ==========================================

from unittest.mock import patch


# ==========================================
# 1. Original Function
# ==========================================

def get_customer_name():
    return "John"


# ==========================================
# 2. Test with Patch
# ==========================================

@patch("__main__.get_customer_name")
def test_customer(mock_get):

    mock_get.return_value = "Michael"

    result = get_customer_name()

    print(f"Inside test: {result}")


# ==========================================
# 3. Run
# ==========================================

print(f"Before test: {get_customer_name()}")

test_customer()

print(f"After test: {get_customer_name()}")