# ==========================================
# Python 87 - Order Validation Tests
# ==========================================

from uuid import UUID

import pytest

from pydantic import ValidationError

from models import Order


# ==========================================
# 1. Test Valid Order
# ==========================================

def test_valid_order():

    order = Order(
        order_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        customer_name="Ahmet",
        product_name="Laptop",
        quantity=2,
        unit_price=25000
    )

    assert order.customer_name == "Ahmet"
    assert order.quantity == 2


# ==========================================
# 2. Test Invalid Quantity
# ==========================================

def test_invalid_quantity():

    with pytest.raises(ValidationError):

        Order(
            order_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
            customer_name="Ayse",
            product_name="Mouse",
            quantity=-3,
            unit_price=500
        )


# ==========================================
# 3. Test Total Price
# ==========================================

def test_total_price():

    order = Order(
        order_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        customer_name="Mehmet",
        product_name="Monitor",
        quantity=3,
        unit_price=4000
    )

    assert order.total_price == 12000


# ==========================================
# 4. Test Invalid UUID
# ==========================================

def test_invalid_uuid():

    with pytest.raises(ValidationError):

        Order(
            order_id="INVALID-ID",
            customer_name="Zeynep",
            product_name="Keyboard",
            quantity=1,
            unit_price=1500
        )