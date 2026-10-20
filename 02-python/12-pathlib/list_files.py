# ==========================================
# Python 79 - List Files
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

reports_dir = base_dir / "reports"


# ==========================================
# 2. Create Sample Files
# ==========================================

reports_dir.mkdir(parents=True, exist_ok=True)

(reports_dir / "sales.csv").touch()
(reports_dir / "customers.csv").touch()
(reports_dir / "notes.txt").touch()


# ==========================================
# 3. List All Files
# ==========================================

print("All files:")

for file in reports_dir.iterdir():
    if file.is_file():
        print(file.name)


# ==========================================
# 4. List Only CSV Files
# ==========================================

print("\nCSV files:")

for file in reports_dir.glob("*.csv"):
    print(file.name)