# ==========================================
# Python 87 - Validator Transformation
# ==========================================

from pydantic import BaseModel, field_validator


# ==========================================
# 1. Define Customer Model
# ==========================================

class Customer(BaseModel):
    customer_id: int
    name: str

    # ==========================================
    # 2. Normalize Customer Name
    # ==========================================

    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:

        cleaned_name = value.strip().title()

        return cleaned_name


# ==========================================
# 3. Create Customer
# ==========================================

customer = Customer(
    customer_id=1001,
    name="   ahmet yılmaz   "
)


# ==========================================
# 4. Display Customer Information
# ==========================================

print(f"Customer ID: {customer.customer_id}")
print(f"Customer Name: {customer.name}")