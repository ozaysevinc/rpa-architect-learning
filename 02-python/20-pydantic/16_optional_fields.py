# ==========================================
# Python 87 - Optional Fields
# ==========================================

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Order Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    customer_name: str = Field(min_length=2)
    discount_code: str | None = None


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "customer_name": "Ahmet"
}


# ==========================================
# 3. Validate API Response
# ==========================================

order = OrderResponse.model_validate(api_response)


# ==========================================
# 4. Display Order Information
# ==========================================

print(f"Order ID: {order.order_id}")
print(f"Customer: {order.customer_name}")
print(f"Discount Code: {order.discount_code}")