bot_list = ["InvoiceBot","ReportBot","SapBot","EmailBot"]
# print(bot_list[0])
# print(bot_list[2])
# print(bot_list[3])

# bot_list.append("FinanceBot")
# bot_list.remove("ReportBot")
# bot_list[1] = "SAPAutomation"

# print(bot_list)
# print(len(bot_list))

#FOR LOOP
# for bot in bot_list:
#     if bot == "SAPAutomation":
#         print("SAP bot found")
#     else:
#         print("Other bot:", bot)

#RANGE
# for i in range(1, 4):
#     print("Retry attempt:", i )

#WHILE
# attempt = 1
# while attempt <= 5:
#     print("Processing transaction:", attempt)
#     attempt += 1
# print("All transactions completed")

#BREAK and CONTINUE
# for attempt in range(1, 6):
#     print("Attempt:", attempt)

#     if attempt == 3:
#         print("Transaction successful")
#         break

for attempt in range(1, 6):
    if attempt == 3:
        print("Skipping transaction:", attempt)
        continue
    print("Processing transaction:", attempt)