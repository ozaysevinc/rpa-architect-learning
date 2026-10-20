# ==========================================
# Python 79 - Move and Rename Files
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

reports_dir = base_dir / "reports"
processed_dir = base_dir / "processed"

source_file = reports_dir / "finance_report.csv"
target_file = processed_dir / "finance_report_completed.csv"


# ==========================================
# 2. Create Folders
# ==========================================

reports_dir.mkdir(parents=True, exist_ok=True)
processed_dir.mkdir(parents=True, exist_ok=True)


# ==========================================
# 3. Create Sample Report
# ==========================================

source_file.write_text(
    "customer_id,amount\n101,1500\n102,2500",
    encoding="utf-8"
)


# ==========================================
# 4. Move and Rename File
# ==========================================

source_file.rename(target_file)


# ==========================================
# 5. Check Results
# ==========================================

print(f"Source exists: {source_file.exists()}")
print(f"Target exists: {target_file.exists()}")
print(f"Target name: {target_file.name}")