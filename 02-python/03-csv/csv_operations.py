# ==========================================
# 01 - READING CSV FILES
# ==========================================

# import csv

# with open('transactions.csv','r', encoding='utf-8-sig',newline="") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(f"{row['Customer']} - {row['Status']}")

# ==========================================
# 02 - COUNTING TRANSACTION RESULTS
# ==========================================

# import csv

# success_count = 0
# failed_count = 0

# with open('transactions.csv', 'r', encoding='utf-8-sig', newline="") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         if row['Status'] == 'Success':
#             success_count += 1
#         elif row['Status'] == 'Failed':
#             failed_count += 1

# print(f"Success: {success_count}")
# print(f"Failed: {failed_count}")
# print(f"total transactions: {success_count + failed_count}")

# ==========================================
# 03 - CALCULATING SUCCESSFUL AMOUNTS
# ==========================================

# import csv

# total_success_amount = 0

# with open('transactions.csv', 'r', encoding='utf-8-sig', newline="") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         if row['Status'] == 'Success':
#             total_success_amount += int(row['Amount'])

# print(f"Total Successful Amount: {total_success_amount}")

# ==========================================
# 04 - EXPORTING FAILED TRANSACTIONS
# ==========================================

import csv

fieldnames = ["TransactionID", "Customer", "Amount", "Status"]

with open("transactions.csv", "r", encoding="utf-8-sig", newline="") as source_file:
    reader = csv.DictReader(source_file)

    with open("failed_transactions.csv", "w", encoding="utf-8-sig", newline="") as target_file:
        writer = csv.DictWriter(target_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row["Status"] == "Failed":
                writer.writerow(row)
