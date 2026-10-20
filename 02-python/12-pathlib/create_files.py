# ==========================================
# Python 79 - Create Files and Folders
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
# 3. Create Log File
# ==========================================

log_file.write_text(
    "Finance Bot started successfully.",
    encoding="utf-8"
)


# ==========================================
# 4. Check Results
# ==========================================

print(f"Folder exists: {logs_dir.exists()}")
print(f"File exists: {log_file.exists()}")
print(f"Log content: {log_file.read_text(encoding='utf-8')}")