# ==========================================
# 01 - BASIC FUNCTIONS
# ==========================================

# def bot_status():
#     print("Bot is running")

# bot_status()
# bot_status()
# bot_status()

# ==========================================
# 02 - FUNCTION PARAMETERS
# ==========================================

# def check_bot(bot_name, status):
#     print(bot_name + " status:", status)

# check_bot("InvoiceBot", "Success")
# check_bot("SAPBot", "Running")
# check_bot("EmailBot", "Failed")

# ==========================================
# 03 - RETURN VALUES
# ==========================================

# def calculate_success_rate(successful,total):
#     return (successful / total) * 100

# success_rate = calculate_success_rate(180, 200)
# print("Success rate:", success_rate)

# ==========================================
# 04 - FUNCTIONS WITH CONDITIONS
# ==========================================

# def check_performance(success_rate):
#     if success_rate >= 90:
#         return "Excellent"
#     elif success_rate >= 70 and success_rate < 90:
#         return "Good"
#     else:
#         return "Needs Improvement"

# print(check_performance(95))
# print(check_performance(80))
# print(check_performance(50))

# ==========================================
# 05 - DEFAULT PARAMETERS
# ==========================================

def execute_bot(bot_name, retry_count=3):
    print("Executing " + bot_name + " with " + str(retry_count) + " retries")

execute_bot("InvoiceBot")
execute_bot("SAPBot", 5)
execute_bot("EmailBot")