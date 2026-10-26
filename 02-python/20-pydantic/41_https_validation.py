# ==========================================
# Python 87 - HTTPS URL Validation
# ==========================================

from pydantic import (
    BaseModel,
    HttpUrl,
    ValidationError,
    field_validator
)


# ==========================================
# 1. Define API Configuration Model
# ==========================================

class APIConfig(BaseModel):
    bot_name: str
    api_url: HttpUrl
    timeout: int

    # ==========================================
    # 2. Validate HTTPS Connection
    # ==========================================

    @field_validator("api_url")
    @classmethod
    def validate_https(cls, value: HttpUrl) -> HttpUrl:

        if value.scheme != "https":
            raise ValueError(
                "API URL must use HTTPS"
            )

        return value


# ==========================================
# 3. Simulate API Configuration
# ==========================================

config_data = {
    "bot_name": "Finance Bot",
    "api_url": "http://api.example.com/orders",
    "timeout": 30
}


# ==========================================
# 4. Validate Configuration
# ==========================================

try:
    config = APIConfig.model_validate(config_data)

    print("Configuration validated successfully.")
    print(f"API URL: {config.api_url}")

except ValidationError as error:
    print("Configuration validation failed.")

    for detail in error.errors():
        print(f"Field: {detail['loc']}")
        print(f"Message: {detail['msg']}")