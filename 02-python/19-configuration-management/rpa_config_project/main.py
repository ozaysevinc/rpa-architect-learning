# ==========================================
# Python 86 - Finance Bot
# ==========================================

from config_manager import load_config, validate_config


# ==========================================
# 1. Load Configuration
# ==========================================

config = load_config()


# ==========================================
# 2. Validate Configuration
# ==========================================

validate_config(config)


# ==========================================
# 3. Start Finance Bot
# ==========================================

bot_name = config["bot_name"]
timeout = config["timeout"]
max_retries = config["max_retries"]

print(f"Bot Name: {bot_name}")
print(f"Timeout: {timeout}")
print(f"Max Retries: {max_retries}")

print("Finance Bot started.")