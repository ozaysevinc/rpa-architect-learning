processed_count = 75

if processed_count >= 200:
    print("High")
elif processed_count >= 100:
    print("Medium")
else:
    print("Low")


# and or 

status = "Success"
processed_count = 100

if status == "Success" and processed_count >= 200:
    print("Target reached")
elif status == "Success" and processed_count < 200:
    print("Success but below target")
else:
    print("Run Failed")

