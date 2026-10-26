# ==========================================
# Python 87 - API Response Validation
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define API Response Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    customer_name: str = Field(min_length=2)
    total_amount: float = Field(gt=0)
    status: str


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "customer_name": "Ahmet",
    "total_amount": 1250.50,
    "status": "completed"
}


# ==========================================
# 3. Validate API Response
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)

    print("API response validated successfully.")
    print(f"Order ID: {order.order_id}")
    print(f"Customer: {order.customer_name}")
    print(f"Amount: {order.total_amount}")
    print(f"Status: {order.status}")

except ValidationError as error:
    print("API response validation failed.")
    print(error)