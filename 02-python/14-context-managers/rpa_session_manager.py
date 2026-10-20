# ==========================================
# Python 81 - RPA Session Manager
# ==========================================

from contextlib import contextmanager


# ==========================================
# 1. Define Bot Session
# ==========================================

@contextmanager
def bot_session(bot_name: str):

    print(f"Starting session: {bot_name}")

    try:
        yield bot_name

    except Exception as error:
        print(f"Bot error: {error}")
        raise

    finally:
        print(f"Closing session: {bot_name}")


# ==========================================
# 2. Run Finance Bot
# ==========================================

try:

    with bot_session("Finance Bot") as bot:

        print(f"{bot} is processing payments")

        amount = 1500

        if amount <= 0:
            raise ValueError("Invalid payment amount")

        print("Payment processed successfully")

except Exception as error:

    print(f"Main application caught: {error}")