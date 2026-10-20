# ==========================================
# Python 79 - Finance Report Processor
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

incoming_dir = base_dir / "incoming"
processed_dir = base_dir / "processed"


# ==========================================
# 2. Create Folders
# ==========================================

incoming_dir.mkdir(parents=True, exist_ok=True)
processed_dir.mkdir(parents=True, exist_ok=True)


# ==========================================
# 3. Create Sample Reports
# ==========================================

report_1 = incoming_dir / "finance_january.csv"
report_2 = incoming_dir / "finance_february.csv"

report_1.write_text(
    "customer_id,amount\n101,1500\n102,2500",
    encoding="utf-8"
)

report_2.write_text(
    "customer_id,amount\n103,3000\n104,4500",
    encoding="utf-8"
)

# # ==========================================
# # 4. Check Incoming Reports
# # ==========================================

# print("Incoming reports:")

# for report in incoming_dir.glob("*.csv"):
#     print(report.name)

# # ==========================================
# # 5. Process Reports
# # ==========================================

# for report in incoming_dir.glob("*.csv"):

#     print(f"\nProcessing: {report.name}")

#     # Define target path
#     target_file = processed_dir / report.name

#     # Check if target already exists
#     if target_file.exists():
#         print(f"Skipped: {report.name} already exists.")
#         continue

#     # Read report content
#     content = report.read_text(encoding="utf-8")

#     print(content)

#     # Move report
#     report.rename(target_file)

#     print(f"Moved to: {target_file}")