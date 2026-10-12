# ==========================================
# Python 69 - Basic Logging
# ==========================================

import logging


# ==========================================
# 1. Configure Logging with Handlers
# ==========================================

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


# ==========================================
# 2. Simulate RPA Bot Operations
# ==========================================

logging.info("RPA bot started.")

logging.debug("ERP API URL: https://example.com/customers")
logging.debug("Customer ID: 101")

logging.info("Connecting to ERP system.")

logging.info("Customer 101 found.")

logging.warning("Customer 999 not found.")

logging.error("ERP connection failed.")

logging.critical("ERP system is completely unavailable.")

logging.info("RPA bot finished.")