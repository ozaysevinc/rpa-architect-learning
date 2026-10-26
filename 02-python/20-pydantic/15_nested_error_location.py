# ==========================================
# Python 87 - Nested Error Location
# ==========================================

from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. Define Product Model
# ==========================================

class Product(BaseModel):
    product_id: int
    name: str
    price: float = Field(gt=0)


# ==========================================
# 2. Define Order Model
# ==========================================

class OrderResponse(BaseModel):
    order_id: int
    products: list[Product]


# ==========================================
# 3. Simulate Invalid API Response
# ==========================================

api_response = {
    "order_id": 1001,
    "products": [
        {
            "product_id": 101,
            "name": "Keyboard",
            "price": 750
        },
        {
            "product_id": 102,
            "name": "Mouse",
            "price": -100
        }
    ]
}


# ==========================================
# 4. Validate and Inspect Errors
# ==========================================

try:
    order = OrderResponse.model_validate(api_response)
    print("Order validated successfully.")

except ValidationError as error:
    for detail in error.errors():
        print(f"Location: {detail['loc']}")
        print(f"Message: {detail['msg']}")
        print(f"Invalid Value: {detail['input']}")