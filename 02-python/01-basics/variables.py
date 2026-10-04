bot_name = "InvoiceBot"
department = "Finance"
status = "Success"
processed = 250
success_rate = 98.5
active = True

print("Bot Name:", bot_name)
print("Department:", department)
print("Status:", status)
print("Processed:", processed)
print("Success Rate:", success_rate)
print("Active:", active)

print(type(bot_name))
print(type(processed))
print(type(success_rate))
print(type(active))

processed = "350"
success_rate = "97.5"

processed_number = int(processed)
success_rate_number = float(success_rate)

print(type(processed_number))
print(type(success_rate_number))

processed_count = 180
target_count = 200

print(processed_count > target_count)
print(processed_count == target_count)
print(processed_count < target_count)
print(processed_count >= 100)