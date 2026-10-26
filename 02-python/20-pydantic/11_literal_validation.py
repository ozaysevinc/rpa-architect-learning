# ==========================================
# Python 87 - Literal Validation
# ==========================================

from typing import Literal
from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Order Response Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    customer_name: str = Field(min_length=2)
    total_amount: float = Field(gt=0)

    status: Literal[
        "pending",
        "processing",
        "completed",
        "cancelled"
    ]


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
    print(f"Order Status: {order.status}")

except ValidationError as error:
    print("API response validation failed.")
    print(error)