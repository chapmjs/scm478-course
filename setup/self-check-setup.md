# Self-Check Setup — Troubleshooting Guide

If `python setup/self_check.py` reports failures, use this guide.

---

## Running the Self-Check

From the root of the course repo:

```bash
python setup/self_check.py
```

Or run checks for a specific unit:

```bash
python setup/self_check.py --unit 1
```

---

## Common Failures

### Python version too old

```
FAIL  Python 3.11+       Found: 3.9.x
```

**Fix:** Download and install Python 3.11+ from python.org. Make sure to check "Add Python to PATH" on Windows.

---

### Package not found

```
FAIL  streamlit          Not installed
```

**Fix:**
```bash
pip install streamlit pandas plotly openpyxl
```

If `pip` is not found, try `python -m pip install ...`

---

### Data file missing

```
FAIL  Products___Pricing.csv    Not found in data/
```

**Fix:** Copy the CSV files from the source provided on Canvas into the `data/` folder. The self-check will not pass without them.

---

### Streamlit won't launch

**Fix:** Try running a minimal test:
```bash
python -m streamlit hello
```

If that fails, reinstall: `pip install --upgrade streamlit`

---

## Unit-Specific Checks

| Unit | Check file | What it tests |
|------|-----------|---------------|
| 1 | `checks/unit1_checks.py` | Python version, packages, Week 1 CSV files |

More unit checks will be added as the course progresses.

---

## Still Stuck?

Post in the Canvas discussion board with:
1. The full output of `python setup/self_check.py`
2. The output of `python --version`
3. Your operating system
