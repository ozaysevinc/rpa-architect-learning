# ==========================================
# Python 87 - Email Validation
# ==========================================

from pydantic import BaseModel, EmailStr, ValidationError


# ==========================================
# 1. Define Customer Model
# ==========================================

class Customer(BaseModel):
    customer_id: int
    customer_name: str
    email: EmailStr


# ==========================================
# 2. Simulate Customer Data
# ==========================================

customer_data = {
    "customer_id": 1001,
    "customer_name": "Ahmet",
    "email": "ahmet@example.com"
}


# ==========================================
# 3. Validate Customer Data
# ==========================================

try:
    customer = Customer.model_validate(customer_data)

    print("Customer validated successfully.")
    print(f"Customer: {customer.customer_name}")
    print(f"Email: {customer.email}")

except ValidationError as error:
    print("Customer validation failed.")
    print(error)