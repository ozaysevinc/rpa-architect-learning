# ==========================================
# Python 73 - RPA Framework
# Base Bot Class
# ==========================================


# ==========================================
# 1. Base RPA Bot
# ==========================================

class RPABot:

    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.status = "Stopped"

    def start(self):
        self.status = "Running"
        print(f"{self.bot_name} started.")

    def process(self):
        raise NotImplementedError(
            "Child classes must implement process()."
        )

    def stop(self):
        self.status = "Stopped"
        print(f"{self.bot_name} stopped.")

