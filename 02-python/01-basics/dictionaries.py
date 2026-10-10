# ==========================================
# 01 - DICTIONARY CREATION
# ==========================================

bot_info = {
    "name": "SAPBot",
    "department": "Finance",
    "status": "Running",
    "processed_count": 120,
    "active": True
}


# ==========================================
# 02 - ACCESSING DICTIONARY VALUES
# ==========================================

# print(bot_info["name"])
# print(bot_info["status"])
# print(bot_info["processed_count"])


# ==========================================
# 03 - UPDATING AND ADDING VALUES
# ==========================================

# bot_info["status"] = "Completed"
# bot_info["processed_count"] = 250
# bot_info["environment"] = "Production"
# del bot_info["active"]

# print(bot_info)


# ==========================================
# 04 - REMOVING DICTIONARY ITEMS
# ==========================================

# del bot_info["active"]


# ==========================================
# 05 - ITERATING THROUGH A DICTIONARY
# ==========================================

# for key, value in bot_info.items():
#     print("Bot Detail -", key + ":", value)

for key, value in bot_info.items():
    
    if key == "department":
        continue
    print("Bot Detail -", key + ":", value)   
    