# ==========================================
# Python 79 - Delete Files
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

temp_dir = base_dir / "temp"
temp_file = temp_dir / "temporary_report.csv"


# ==========================================
# 2. Create Temporary File
# ==========================================

temp_dir.mkdir(parents=True, exist_ok=True)

temp_file.write_text(
    "customer_id,amount\n101,1500",
    encoding="utf-8"
)

print(f"Before deletion: {temp_file.exists()}")


# ==========================================
# 3. Delete File
# ==========================================

if temp_file.exists():
    temp_file.unlink()
    print("Temporary file deleted.")


# ==========================================
# 4. Check Result
# ==========================================

print(f"After deletion: {temp_file.exists()}")