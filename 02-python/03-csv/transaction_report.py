# ==========================================
# 01 - RPA TRANSACTION REPORT
# ==========================================

import csv

def generate_report():
    with open("transactions.csv", "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        
        success_count = 0
        failed_count = 0
        total_count = 0
        total_success_amount = 0
        
        for row in reader:
            total_count += 1
            if row['Status'] == 'Success':
                total_success_amount += int(row['Amount'])
                success_count += 1
            elif row['Status'] == 'Failed':
                failed_count += 1        
        if total_count > 0:
            success_rate = (success_count / total_count) * 100
        else:
            success_rate = 0

        report = f"========== RPA TRANSACTION REPORT ==========\nTotal Transactions: {total_count}\nSuccessful Transactions: {success_count}\nFailed Transactions: {failed_count}\nTotal Successful Amount: {total_success_amount}\nSuccess Rate: {success_rate:.1f}%\n============================================"
        print(report)
    with open("transaction_summary.txt", "w", encoding="utf-8") as file:
        file.write(report)

generate_report()