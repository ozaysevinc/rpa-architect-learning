from datetime import datetime

# ==========================================
# 01 - RPA EXECUTION LOGGER
# ==========================================

def log_execution(bot_name, status, processed_count):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open("execution_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{formatted_time} | {bot_name} | {status} | {processed_count}\n")


log_execution("InvoiceBot", "Success", 250)
log_execution("SAPBot", "Failed", 120)