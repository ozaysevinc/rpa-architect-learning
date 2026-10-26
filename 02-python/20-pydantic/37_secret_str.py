# ==========================================
# Python 87 - SecretStr
# ==========================================

from pydantic import BaseModel, SecretStr


# ==========================================
# 1. Define Bot Configuration Model
# ==========================================

class BotConfig(BaseModel):
    bot_name: str
    api_url: str
    api_key: SecretStr


# ==========================================
# 2. Create Bot Configuration
# ==========================================

config = BotConfig(
    bot_name="Finance Bot",
    api_url="https://api.example.com",
    api_key="demo-api-key-12345"
)


# ==========================================
# 3. Print Configuration
# ==========================================

print(config)


# ==========================================
# 4. Access Secret Field
# ==========================================

print(f"API Key: {config.api_key}")


# ==========================================
# 5. Export Configuration
# ==========================================

print(config.model_dump())

print(config.model_dump_json())