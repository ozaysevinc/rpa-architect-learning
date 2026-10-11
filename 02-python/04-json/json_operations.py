# ==========================================
# Python 43 - JSON Basics
# ==========================================

import json

# ==========================================
# 1. Python Dictionary
# ==========================================

bot_info = {
    "bot_name": "InvoiceBot",
    "version": 1.0,
    "is_active": True,
    "total_transactions": 150
}

# ==========================================
# 2. Convert Dictionary to JSON
# ==========================================

# json_data = json.dumps(bot_info, indent=4)

# print(json_data)
# print(type(json_data))

# ==========================================
# 3. Convert JSON back to Dictionary
# ==========================================

# parsed_data = json.loads(json.dumps(bot_info))

# print(parsed_data)
# print(type(parsed_data))

# print(parsed_data["bot_name"])
# print(parsed_data["total_transactions"])
# print(parsed_data["is_active"])

# ==========================================
# 4. Write Dictionary to JSON File
# ==========================================

# with open("bot_config.json", "w", encoding="utf-8") as file:
#     json.dump(bot_info, file, indent=4)

# print("Bot configuration saved successfully.")

# ==========================================
# 5. Read Dictionary from JSON File
# ==========================================

with open("bot_config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(loaded_config)
print(type(loaded_config))
print(loaded_config["bot_name"])