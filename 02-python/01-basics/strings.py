# ==========================================
# 01 - STRING CLEANING AND FORMATTING
# ==========================================

# bot_name = "   SAPBot   "
# status = "SUCCESS"
# message = "InvoiceBot Failed"

# print(bot_name.strip())  # Remove leading and trailing whitespace
# print(status.lower())    # Convert to lowercase
# print(message.replace("Failed", "Completed"))  # Replace substring

# ==========================================
# 02 - SPLIT AND F-STRINGS
# ==========================================

# bot_log = "SAPBot,Completed,350"

# bot_details = bot_log.split(",")  # Split the string into a list
# bot_name = bot_details[0]
# status = bot_details[1]
# processed_count = bot_details[2]

# print(f"Bot: {bot_name}\nStatus: {status}\nProcessed Transactions: {processed_count}")

# ==========================================
# 03 - STRING TO INTEGER CONVERSION
# ==========================================

# bot_log = "InvoiceBot,Success,450"

# bot_details = bot_log.split(",")  # Split the string into a list
# bot_name = bot_details[0]
# status = bot_details[1]
# processed_count = int(bot_details[2])  # Convert to integer
# if processed_count >= 400:
#     print(f"Bot: {bot_name}\nProcessed: {processed_count}\nTarget reached")
# else:
#     print(f"Bot: {bot_name}\nProcessed: {processed_count}\nBelow target")

# ==========================================
# 04 - STRING VALIDATION
# ==========================================

file_name = "Invoice_Report_2026.xlsx"

if file_name.startswith("Invoice") and file_name.endswith(".xlsx") and "Report" in file_name:
    print("Valid invoice report file")
else:
    print("Invalid file")


