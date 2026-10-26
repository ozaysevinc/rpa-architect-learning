# ==========================================
# Python 87 - Secret API Authentication
# ==========================================

from pydantic import BaseModel, SecretStr


# ==========================================
# 1. Define API Configuration Model
# ==========================================

class APIConfig(BaseModel):
    api_url: str
    api_key: SecretStr


# ==========================================
# 2. Create API Configuration
# ==========================================

config = APIConfig(
    api_url="https://api.example.com",
    api_key="demo-secret-key-123"
)


# ==========================================
# 3. Display Safe Configuration
# ==========================================

print("API Configuration:")
print(config)


# ==========================================
# 4. Prepare Authorization Header
# ==========================================

headers = {
    "Authorization": (
        f"Bearer {config.api_key.get_secret_value()}"
    ),
    "Content-Type": "application/json"
}


# ==========================================
# 5. Check Prepared Header
# ==========================================

print("Authorization header prepared.")

print("Authorization exists:", "Authorization" in headers)

print(
    "Bearer authentication:",
    headers["Authorization"].startswith("Bearer ")
)