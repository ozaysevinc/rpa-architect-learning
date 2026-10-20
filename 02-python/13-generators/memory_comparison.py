# ==========================================
# Python 80 - Memory Comparison
# ==========================================

import sys


# ==========================================
# 1. Normal List
# ==========================================

numbers_list = [number for number in range(1_000_000)]


# ==========================================
# 2. Generator
# ==========================================

numbers_generator = (number for number in range(1_000_000))


# ==========================================
# 3. Compare Memory
# ==========================================

print(f"List size: {sys.getsizeof(numbers_list)} bytes")

print(f"Generator size: {sys.getsizeof(numbers_generator)} bytes")


# ==========================================
# 4. Read Generator Values
# ==========================================

print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))