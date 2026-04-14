"""
Unit 1 self-checks: verifies the CSV files needed for Week 1 are present
and have the expected structure.
"""

from pathlib import Path

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

# Path to data/ relative to the repo root (two levels up from this file)
DATA_DIR = Path(__file__).parent.parent.parent / "data"

REQUIRED_FILES = {
    "Products___Pricing.csv": [
        "SKU", "Product Name", "Description", "Category",
        "Unit of Measure", "Retail Price",
    ],
    "Ingredient_Catalog.csv": [
        "Ingredient SKU", "Description", "Order Unit", "Cost Per Unit",
        "MOQ", "Primary Supplier ID", "Primary Supplier Name",
    ],
}


def check_csv(filename, expected_columns):
    filepath = DATA_DIR / filename
    if not filepath.exists():
        print(f"  {FAIL}  {filename:<35} File not found in data/")
        return False

    try:
        import pandas as pd
        df = pd.read_csv(filepath)
        missing = [c for c in expected_columns if c not in df.columns]
        if missing:
            print(f"  {FAIL}  {filename:<35} Missing columns: {missing}")
            return False
        print(f"  {PASS}  {filename:<35} {len(df)} rows, columns OK")
        return True
    except Exception as e:
        print(f"  {FAIL}  {filename:<35} Error reading file: {e}")
        return False


def run_checks():
    results = []
    for filename, columns in REQUIRED_FILES.items():
        results.append(check_csv(filename, columns))
    passed = sum(results)
    print(f"  Unit 1 data: {passed}/{len(results)} files OK")
