# ==========================================
# Python 87 - Nested Models
# ==========================================

from pydantic import BaseModel, Field


# ==========================================
# 1. Define Customer Model
# ==========================================

class Customer(BaseModel):
    customer_id: int
    name: str = Field(min_length=2)
    email: str


# ==========================================
# 2. Define Order Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    customer: Customer
    total_amount: float = Field(gt=0)


# ==========================================
# 3. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "customer": {
        "customer_id": 501,
        "name": "Ahmet",
        "email": "ahmet@example.com"
    },
    "total_amount": 1250.50
}


# ==========================================
# 4. Validate API Response
# ==========================================

order = OrderResponse.model_validate(api_response)


# ==========================================
# 5. Access Nested Data
# ==========================================

print(f"Order ID: {order.order_id}")
print(f"Customer ID: {order.customer.customer_id}")
print(f"Customer Name: {order.customer.name}")
print(f"Customer Email: {order.customer.email}")
print(f"Total Amount: {order.total_amount}")