# ==========================================
# Python 87 - Allow Extra Fields
# ==========================================

from pydantic import BaseModel, ConfigDict


# ==========================================
# 1. Define Order Response Model
# ==========================================

class OrderResponse(BaseModel):

    model_config = ConfigDict(extra="allow")

    order_id: int
    customer_name: str


# ==========================================
# 2. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "customer_name": "Ahmet",
    "currency": "TRY",
    "source": "mobile"
}


# ==========================================
# 3. Validate API Response
# ==========================================

order = OrderResponse.model_validate(api_response)


# ==========================================
# 4. Access Model Data
# ==========================================

print(f"Order ID: {order.order_id}")
print(f"Customer: {order.customer_name}")

print(f"Currency: {order.currency}")
print(f"Source: {order.source}")


# ==========================================
# 5. Convert Model to Dictionary
# ==========================================

print(order.model_dump())