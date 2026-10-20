# ==========================================
# Python 80 - Basic Generators
# ==========================================


# ==========================================
# 1. Define Generator
# ==========================================

def generate_numbers():

    print("Generating first number")
    yield 1

    print("Generating second number")
    yield 2

    print("Generating third number")
    yield 3


# ==========================================
# 2. Create Generator Object
# ==========================================

numbers = generate_numbers()

print("Generator created")


# ==========================================
# 3. Get Values
# ==========================================

print(next(numbers))
print(next(numbers))
print(next(numbers))
