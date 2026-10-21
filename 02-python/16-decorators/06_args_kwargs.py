# ==========================================
# Python 83 - Args and Kwargs
# ==========================================


# ==========================================
# 1. Understanding *args
# ==========================================

def process_orders(*args):

    print(args)

    for order_id in args:
        print(f"Processing order: {order_id}")


# ==========================================
# 2. Run Function
# ==========================================

process_orders(1001, 1002, 1003)

# ==========================================
# 3. Understanding **kwargs
# ==========================================

def process_order(**kwargs):

    print(kwargs)


# ==========================================
# 4. Run Function
# ==========================================

process_order(
    order_id=1001,
    customer="Ahmet",
    amount=2500
)