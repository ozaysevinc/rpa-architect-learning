# ==========================================
# Python 75 - Unit Testing
# First Unit Test
# ==========================================

import unittest

from calculator import calculate_total


# ==========================================
# 1. Calculator Tests
# ==========================================

class TestCalculator(unittest.TestCase):

    def test_calculate_total(self):
        result = calculate_total(100, 3)
        self.assertEqual(result, 300)

    def test_zero_quantity(self):
        result = calculate_total(100, 0)
        self.assertEqual(result, 0)

    def test_decimal_price(self):
        result = calculate_total(12.5, 4)
        self.assertEqual(result, 50.0)

    # ==========================================
    # 2. Error Scenario Test
    # ==========================================

    def test_negative_quantity(self):

        with self.assertRaises(ValueError):
            calculate_total(100, -3)


# ==========================================
# 2. Run Tests
# ==========================================

if __name__ == "__main__":
    unittest.main()