# ==========================================
# Python 81 - Context Manager Errors
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

        if exc_type is not None:
            print(f"Error type: {exc_type.__name__}")
            print(f"Error message: {exc_value}")

        return True


# ==========================================
# 2. Run Bot
# ==========================================

print("Before with")

with BotSession() as session:

    print("Processing payment")

    result = 100 / 0

    print("Payment completed")

print("After with")