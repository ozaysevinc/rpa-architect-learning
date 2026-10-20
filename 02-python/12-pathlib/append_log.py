# ==========================================
# Python 79 - Append to Log File
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

logs_dir = base_dir / "logs"

log_file = logs_dir / "finance_bot.log"


# ==========================================
# 2. Create Folder
# ==========================================

logs_dir.mkdir(parents=True, exist_ok=True)


# ==========================================
# 3. Append Log
# ==========================================

with log_file.open("a", encoding="utf-8") as file:
    file.write("Finance Bot processed a customer.\n")


# ==========================================
# 4. Read Log
# ==========================================

print(log_file.read_text(encoding="utf-8"))