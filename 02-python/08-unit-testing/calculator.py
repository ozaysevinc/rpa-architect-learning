# ==========================================
# Python 75 - Unit Testing
# Calculator Functions
# ==========================================

def calculate_total(price, quantity):

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return price * quantity