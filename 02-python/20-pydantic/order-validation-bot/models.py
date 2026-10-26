# ==========================================
# Python 87 - Order Validation Models
# ==========================================

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, computed_field


# ==========================================
# 1. Order Model
# ==========================================

class Order(BaseModel):
    order_id: UUID
    customer_name: str = Field(min_length=2)
    product_name: str = Field(min_length=2)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price


# ==========================================
# 2. Validation Report Model
# ==========================================

class ValidationReport(BaseModel):
    execution_id: UUID = Field(default_factory=uuid4)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    total_orders: int
    valid_orders: int
    invalid_orders: int