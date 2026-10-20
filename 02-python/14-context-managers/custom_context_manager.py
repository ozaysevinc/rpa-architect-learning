# ==========================================
# Python 81 - Custom Context Manager
# ==========================================


# ==========================================
# 1. Define Context Manager
# ==========================================

class BotSession:

    def __enter__(self):

        print("Bot session started")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Bot session closed")


# ==========================================
# 2. Use Context Manager
# ==========================================

print("Before with")

with BotSession() as session:

    print("Finance Bot is processing payments")

print("After with")