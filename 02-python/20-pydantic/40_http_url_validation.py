# ==========================================
# Python 87 - HTTP URL Validation
# ==========================================

from pydantic import (
    BaseModel,
    HttpUrl,
    ValidationError
)


# ==========================================
# 1. Define API Configuration Model
# ==========================================

class APIConfig(BaseModel):
    bot_name: str
    api_url: HttpUrl
    timeout: int


# ==========================================
# 2. Simulate API Configuration
# ==========================================

config_data = {
    "bot_name": "Finance Bot",
    "api_url": "https://api.example.com/orders",
    "timeout": 30
}


# ==========================================
# 3. Validate Configuration
# ==========================================

try:
    config = APIConfig.model_validate(config_data)

    print("Configuration validated successfully.")
    print(f"Bot: {config.bot_name}")
    print(f"API URL: {config.api_url}")
    print(f"Timeout: {config.timeout}")

except ValidationError as error:
    print("Configuration validation failed.")
    print(error)