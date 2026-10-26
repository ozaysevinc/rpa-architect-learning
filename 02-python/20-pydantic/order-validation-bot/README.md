# Order Validation Bot

A Python RPA mini project that validates e-commerce order data using Pydantic v2.

## Features

- Validate incoming order records
- Validate UUIDs, quantities, prices, and text fields
- Calculate order totals automatically
- Separate valid and invalid orders
- Generate a JSON validation report
- Track executions with UUIDs and UTC timestamps
- Run automated tests with pytest

## Technologies

- Python
- Pydantic v2
- pytest
- JSON
- pathlib

## Project Structure

```text
order-validation-bot/
├── main.py
├── models.py
├── test_models.py
├── README.md
└── reports/
    └── validation_report.json
```

## Run the Bot

From the repository root:

```powershell
python 02-python/20-pydantic/order-validation-bot/main.py
```

## Run Tests

```powershell
python -m pytest "02-python/20-pydantic/order-validation-bot/test_models.py" -v
```

## Validation Rules

- Order IDs must be valid UUIDs.
- Customer and product names must contain at least two characters.
- Quantities must be greater than zero.
- Unit prices must be greater than zero.
- Total prices are calculated automatically.

## Expected Results

The sample dataset contains four orders:

- 2 valid orders
- 2 invalid orders

Invalid records are captured without stopping the entire validation process.

## Test Results

All four automated tests passed.

## Learning Objectives

Practice Pydantic data validation, computed fields, error handling, JSON serialization, and automated testing in an RPA-oriented scenario.