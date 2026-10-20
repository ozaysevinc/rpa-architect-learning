# ==========================================
# Python 81 - Contextmanager Decorator
# ==========================================

from contextlib import contextmanager


# ==========================================
# 1. Define Context Manager
# ==========================================

@contextmanager
def bot_session():

    print("Bot session started")

    try:
        yield "Finance Bot"

    finally:
        print("Bot session closed")


# ==========================================
# 2. Use Context Manager
# ==========================================

print("Before with")

with bot_session() as bot:

    print(f"{bot} is processing payments")

print("After with")