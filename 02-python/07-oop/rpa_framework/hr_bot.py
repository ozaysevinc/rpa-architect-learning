# ==========================================
# Python 73 - RPA Framework
# HR Bot
# ==========================================

from base_bot import RPABot


# ==========================================
# 1. HR Bot Class
# ==========================================

class HRBot(RPABot):

    def process(self):
        print(f"{self.bot_name} is processing employee records.")


# ==========================================
# 2. Test HR Bot
# ==========================================

if __name__ == "__main__":

    hr_bot = HRBot("EmployeeBot")

    hr_bot.start()
    hr_bot.process()
    hr_bot.stop()