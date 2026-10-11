import json
import sys

try:
    with open("bot_config.json", "r", encoding="utf-8") as file:
        loaded_config = json.load(file)

    print(f"Bot Name: {loaded_config['bot_name']}")
    print(f"Environment: {loaded_config['environment']}")

    if loaded_config["is_active"] == True:
        print("Bot is ready to run.")
    else:
        print("Bot is disabled.")

    for counter in range(loaded_config["max_retries"]):
        print(f"Attempt: {counter + 1}")
except FileNotFoundError:
    print("Configuration file not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Invalid JSON format.")
    sys.exit(1)