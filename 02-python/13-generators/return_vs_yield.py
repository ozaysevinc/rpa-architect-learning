# ==========================================
# Python 80 - Return vs Yield
# ==========================================


# ==========================================
# 1. Normal Function
# ==========================================

def get_numbers():

    print("Normal function started")

    return [1, 2, 3]


# ==========================================
# 2. Generator Function
# ==========================================

def generate_numbers():

    print("Generator started")

    yield 1
    yield 2
    yield 3


# ==========================================
# 3. Test Normal Function
# ==========================================

numbers = get_numbers()

print(numbers)


# ==========================================
# 4. Test Generator
# ==========================================

generator = generate_numbers()

print("Generator object created")

for number in generator:
    print(number)