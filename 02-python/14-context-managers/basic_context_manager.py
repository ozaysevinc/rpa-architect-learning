# ==========================================
# Python 81 - Basic Context Manager
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define File Path
# ==========================================

base_dir = Path(__file__).resolve().parent

file_path = base_dir / "finance_report.txt"


# ==========================================
# 2. Write File Using With
# ==========================================

with file_path.open("w", encoding="utf-8") as file:

    file.write("Finance Bot started.\n")
    file.write("Finance Bot completed.\n")

    print(f"Inside with - File closed: {file.closed}")


# ==========================================
# 3. Check File Status
# ==========================================

print(f"Outside with - File closed: {file.closed}")


# ==========================================
# 4. Read File
# ==========================================

with file_path.open("r", encoding="utf-8") as file:

    content = file.read()

    print("\nFile content:")
    print(content)