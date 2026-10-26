# ==========================================
# Python 87 - Custom Field Validator
# ==========================================

from pydantic import BaseModel, field_validator, ValidationError


# ==========================================
# 1. Define Customer Model
# ==========================================

class Customer(BaseModel):
    customer_id: str
    name: str

    # ==========================================
    # 2. Validate Customer ID
    # ==========================================

    @field_validator("customer_id")
    @classmethod
    def validate_customer_id(cls, value: str) -> str:

        if not value.startswith("CUS-"):
            raise ValueError("Customer ID must start with CUS-")

        return value


# ==========================================
# 3. Create Customer
# ==========================================

try:
    customer = Customer(
        customer_id="CUS-1001",
        name="Ahmet"
    )

    print("Customer validated successfully.")
    print(f"Customer ID: {customer.customer_id}")

except ValidationError as error:
    print("Customer validation failed.")
    print(error)