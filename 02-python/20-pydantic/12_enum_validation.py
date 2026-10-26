# ==========================================
# Python 87 - Enum Validation
# ==========================================

from enum import Enum
from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Order Status Enum
# ==========================================

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


# ==========================================
# 2. Define Order Response Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    total_amount: float = Field(gt=0)
    status: OrderStatus


# ==========================================
# 3. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "total_amount": 1250.50,
    "status": "completed"
}


# ==========================================
# 4. Validate API Response
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)

    print("API response validated successfully.")
    print(f"Order Status: {order.status.value}")

    if order.status == OrderStatus.COMPLETED:
        print("Order is ready for processing.")

except ValidationError as error:
    print("API response validation failed.")
    print(error)