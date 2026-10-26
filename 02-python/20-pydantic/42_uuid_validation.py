# ==========================================
# Python 87 - UUID Validation
# ==========================================

from uuid import UUID

from pydantic import BaseModel, ValidationError


# ==========================================
# 1. Define Order Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: UUID
    customer_name: str
    amount: float


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "order_id": "550e8400-e29b-41d4-a716-446655440000",
    "customer_name": "Ahmet",
    "amount": 1250.50
}


# ==========================================
# 3. Validate API Response
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)

    print("Order validated successfully.")
    print(f"Order ID: {order.order_id}")
    print(f"Customer: {order.customer_name}")
    print(f"Amount: {order.amount}")

except ValidationError as error:
    print("Order validation failed.")
    print(error)


# ==========================================
# 4. Check Order ID Type
# ==========================================

if "order" in locals():
    print(f"Order ID Type: {type(order.order_id)}")