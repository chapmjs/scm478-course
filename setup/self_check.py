"""
SCM 478 Self-Check Script
Run this from the root of the course repo:
    python setup/self_check.py

Optional: run checks for a specific unit:
    python setup/self_check.py --unit 1
"""

import sys
import argparse
from pathlib import Path

# Ensure the setup/ directory is on the path so checks/ can be imported
SETUP_DIR = Path(__file__).parent
sys.path.insert(0, str(SETUP_DIR))

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
WARN = "\033[93mWARN\033[0m"


def check_python_version():
    major, minor = sys.version_info[:2]
    label = f"Python {major}.{minor}.{sys.version_info[2]}"
    if major == 3 and minor >= 11:
        print(f"  {PASS}  Python 3.11+       {label}")
        return True
    else:
        print(f"  {FAIL}  Python 3.11+       Found: {label} (upgrade required)")
        return False


def check_package(name, import_name=None):
    import_name = import_name or name
    try:
        __import__(import_name)
        print(f"  {PASS}  {name}")
        return True
    except ImportError:
        print(f"  {FAIL}  {name:<20} Not installed  →  pip install {name}")
        return False


def run_unit_checks(unit_number):
    try:
        module_name = f"checks.unit{unit_number}_checks"
        mod = __import__(module_name, fromlist=["run_checks"])
        mod.run_checks()
    except ModuleNotFoundError:
        print(f"  {WARN}  No checks found for unit {unit_number}")


def main():
    parser = argparse.ArgumentParser(description="SCM 478 environment self-check")
    parser.add_argument("--unit", type=int, help="Run checks for a specific unit only")
    args = parser.parse_args()

    print("\n=== SCM 478 Self-Check ===\n")

    if args.unit:
        print(f"--- Unit {args.unit} checks ---")
        run_unit_checks(args.unit)
    else:
        print("--- Core environment ---")
        results = []
        results.append(check_python_version())
        results.append(check_package("streamlit"))
        results.append(check_package("pandas"))
        results.append(check_package("plotly"))
        results.append(check_package("openpyxl"))

        print("\n--- Unit 1 checks ---")
        run_unit_checks(1)

        passed = sum(results)
        total = len(results)
        print(f"\nCore: {passed}/{total} passed")

    print()


if __name__ == "__main__":
    main()
