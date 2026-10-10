# ==========================================
# 01 - TRY AND EXCEPT
# ==========================================

# successful = 150
# total = 0

# try:
#     success_rate = (successful / total) * 100
#     print(f"Success Rate: {success_rate}")
# except ZeroDivisionError:
#     print("Error: Division by zero")

# ==========================================
# 02 - MULTIPLE EXCEPT BLOCKS
# ==========================================

# successful = "180"
# total = "0"

# try:
#     processed_count = int(successful)
#     total_count = int(total)

#     success_rate = (processed_count / total_count) * 100
#     print(f"Success rate: {success_rate}")

# except ValueError:
#     print("Error: Invalid number format")

# except ZeroDivisionError:
#     print("Error: Division by zero")

# ==========================================
# 03 - ELSE AND FINALLY
# ==========================================

# transaction_count = "150"

# try:
#     processed_count = int(transaction_count)
# except ValueError:
#     print("Invalid transaction count")
# else:
#     print(f"Processed transactions: {processed_count}")
# finally:
#     print("Bot execution finished")

# ==========================================
# 04 - RPA RETRY MECHANISM
# ==========================================

for attempt in range(1, 6):
    try:
        print(f"Attempt: {attempt}")

        if attempt < 3:
            raise ValueError("Transaction failed")

    except ValueError as e:
        print(e)

    else:
        print("Transaction successful")
        break