# ==========================================
# Python 69 - Rotating File Handler
# ==========================================

import logging
from logging.handlers import RotatingFileHandler


# ==========================================
# 1. Configure Logger
# ==========================================

logger = logging.getLogger("RPABot")

logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    "rotating_bot.log",
    maxBytes=1024,
    backupCount=3,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# ==========================================
# 2. Simulate RPA Bot Operations
# ==========================================

for customer_id in range(1, 201):

    logger.info(
        f"Processing customer {customer_id}"
    )

print("Logging completed.")