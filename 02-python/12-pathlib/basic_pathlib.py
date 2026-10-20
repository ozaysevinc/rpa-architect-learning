# ==========================================
# Python 79 - Pathlib
# ==========================================

from pathlib import Path


# ==========================================
# 1. Create Path Object
# ==========================================

file_path = Path("logs") / "finance_bot_2026.log"

# ==========================================
# 2. Path Information
# ==========================================

print(f"Full path: {file_path}")
print(f"File name: {file_path.name}")
print(f"File extension: {file_path.suffix}")
print(f"File stem: {file_path.stem}")
print(f"Parent folder: {file_path.parent}")