# ==========================================
# Python 87 - Extra Fields Validation
# ==========================================

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError
)


# ==========================================
# 1. Define Order Response Model
# ==========================================

class OrderResponse(BaseModel):

    model_config = ConfigDict(extra="forbid")

    order_id: int
    customer_name: str
    total_amount: float = Field(gt=0)


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "customer_name": "Ahmet",
    "total_amount": 1250.50,
    "unexpected_field": "test"
}


# ==========================================
# 3. Validate API Response
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)

    print("API response validated successfully.")
    print(f"Order ID: {order.order_id}")

except ValidationError as error:
    print("API response validation failed.")

    for detail in error.errors():
        print(f"Field: {detail['loc']}")
        print(f"Message: {detail['msg']}")