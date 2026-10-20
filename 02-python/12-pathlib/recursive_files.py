# ==========================================
# Python 79 - Recursive File Search
# ==========================================

from pathlib import Path


# ==========================================
# 1. Define Paths
# ==========================================

base_dir = Path(__file__).resolve().parent

reports_dir = base_dir / "reports"
archive_dir = reports_dir / "archive"


# ==========================================
# 2. Create Sample Files
# ==========================================

archive_dir.mkdir(parents=True, exist_ok=True)

(reports_dir / "sales.csv").touch()
(reports_dir / "customers.csv").touch()
(archive_dir / "old_sales.csv").touch()


# ==========================================
# 3. Search with glob
# ==========================================

print("GLOB RESULTS:")

for file in reports_dir.glob("*.csv"):
    print(file.name)


# ==========================================
# 4. Search with rglob
# ==========================================

print("\nRGLOB RESULTS:")

for file in reports_dir.rglob("*.csv"):
    print(file.relative_to(reports_dir))