# ==========================================
# Python 87 - Nested List Models
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Product Model
# ==========================================

class Product(BaseModel):
    product_id: int
    name: str = Field(min_length=2)
    price: float = Field(gt=0)


# ==========================================
# 2. Define Order Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    products: list[Product]


# ==========================================
# 3. Simulate API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "products": [
        {
            "product_id": 101,
            "name": "Keyboard",
            "price": 750.0
        },
        {
            "product_id": 102,
            "name": "Mouse",
            "price": 450.0
        }
    ]
}


# ==========================================
# 4. Validate API Response
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)

    # ==========================================
    # 5. Display Products
    # ==========================================

    print(f"Order ID: {order.order_id}")

    for product in order.products:
        print(f"Product: {product.name}")
        print(f"Price: {product.price}")

except ValidationError as error:
    print("API response validation failed.")
    print(error)