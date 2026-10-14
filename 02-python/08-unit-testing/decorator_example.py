# ==========================================
# 1. Decorator
# ==========================================

def my_decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


# ==========================================
# 2. Original Function
# ==========================================

@my_decorator
def say_hello():
    print("Hello!")


# ==========================================
# 3. Run
# ==========================================

say_hello()