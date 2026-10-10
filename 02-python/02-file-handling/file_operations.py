# ==========================================
# 01 - WRITING TO A TEXT FILE
# ==========================================

# with open("bot_log.txt", "w", encoding="utf-8") as file:
#     file.write("Bot Name: InvoiceBot\nStatus: Success\nProcessed Transactions: 250")

# ==========================================
# 02 - READING FROM A TEXT FILE
# ==========================================

# with open("bot_log.txt", "r", encoding="utf-8") as file:
#     bot_log_content = file.read()
#     print(bot_log_content)

# ==========================================
# 03 - APPENDING TO A TEXT FILE
# ==========================================

# with open("bot_log.txt", "a", encoding="utf-8") as file:
#     file.write("\nEnvironment: Production\nExecution Result: Completed")
# with open("bot_log.txt", "r", encoding="utf-8") as file:
#     bot_log_content = file.read()
#     print(bot_log_content)

# ==========================================
# 04 - READING FILE LINE BY LINE
# ==========================================

with open("bot_log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        if "Status" in line or "Execution Result" in line:
            print(line.strip())