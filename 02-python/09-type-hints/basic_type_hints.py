# ==========================================
# Python 76 - Type Hints
# ==========================================

# ==========================================
# 1. Calculate Total
# ==========================================

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


# ==========================================
# 2. Run
# ==========================================

total = calculate_total(125.5, 3)

print(f"Total: {total}")