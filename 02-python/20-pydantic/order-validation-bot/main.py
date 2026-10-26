# ==========================================
# Python 87 - Order Validation Bot
# ==========================================

import json

from pathlib import Path

from pydantic import ValidationError

from models import Order, ValidationReport

# ==========================================
# 4. Simulate API Response
# ==========================================

api_response = [
    {
        "order_id": "550e8400-e29b-41d4-a716-446655440000",
        "customer_name": "Ahmet",
        "product_name": "Laptop",
        "quantity": 2,
        "unit_price": 25000
    },
    {
        "order_id": "6ba7b810-9dad-41d1-80b4-00c04fd430c8",
        "customer_name": "Ayşe",
        "product_name": "Mouse",
        "quantity": -3,
        "unit_price": 500
    },
    {
        "order_id": "invalid-order-id",
        "customer_name": "Mehmet",
        "product_name": "Keyboard",
        "quantity": 1,
        "unit_price": 1500
    },
    {
        "order_id": "123e4567-e89b-42d3-a456-426614174000",
        "customer_name": "Zeynep",
        "product_name": "Monitor",
        "quantity": 1,
        "unit_price": 8000
    }
]


# ==========================================
# 5. Validate Orders
# ==========================================

valid_orders = []
invalid_orders = []

for order_data in api_response:

    try:
        order = Order.model_validate(order_data)

        valid_orders.append(
            order.model_dump(mode="json")
        )

        print(
            f"VALID: {order.customer_name} - "
            f"{order.total_price} TL"
        )

    except ValidationError as error:

        invalid_orders.append({
            "original_data": order_data,
            "errors": error.errors(
                include_url=False,
                include_context=False
            )
        })

        print(
            f"INVALID: {order_data.get('customer_name')}"
        )


# ==========================================
# 6. Create Validation Report
# ==========================================

report = ValidationReport(
    total_orders=len(api_response),
    valid_orders=len(valid_orders),
    invalid_orders=len(invalid_orders)
)


# ==========================================
# 7. Prepare JSON Output
# ==========================================

output_data = {
    "summary": report.model_dump(mode="json"),
    "valid_orders": valid_orders,
    "invalid_orders": invalid_orders
}


# ==========================================
# 8. Save JSON Report
# ==========================================

report_directory = Path(__file__).parent / "reports"

report_directory.mkdir(
    parents=True,
    exist_ok=True
)

report_path = report_directory / "validation_report.json"

with open(report_path, "w", encoding="utf-8") as file:
    json.dump(
        output_data,
        file,
        indent=4,
        ensure_ascii=False
    )


# ==========================================
# 9. Display Summary
# ==========================================

print()
print("========== VALIDATION SUMMARY ==========")

print(f"Total Orders: {report.total_orders}")
print(f"Valid Orders: {report.valid_orders}")
print(f"Invalid Orders: {report.invalid_orders}")

print()
print(f"Report saved: {report_path}")