# Homework 1 — Vendor Tab and Ingredient Detail

**Due:** See Canvas  
**Points:** 10

---

## Overview

Extend your Week 1 catalog app to include supplier information and a detail view for individual ingredients.

---

## New Data File

You will need `data/Vendor_Contacts___Terms.csv` for this assignment. Copy it into your `data/` folder if you haven't already.

---

## Requirements

### Requirement 1 — Vendor Tab (3 pts)

Add a third tab called **Vendors** that displays the `Vendor_Contacts___Terms.csv` table.

- Include a filter by Payment Terms (selectbox with "All" option)
- Display a metric showing the average lead time across all vendors (or filtered vendors)

### Requirement 2 — Ingredient Detail View (3 pts)

On the Ingredients tab, add a selectbox that lets the user pick an ingredient by name. When selected, display the full detail for that ingredient below the table, including:

- Ingredient SKU
- Description
- Cost Per Unit and Order Unit
- MOQ
- Primary Supplier Name

Format it nicely — use `st.write()`, `st.json()`, or a small two-column layout with `st.columns()`.

### Requirement 3 — Supplier Lookup (2 pts)

In the ingredient detail view (Requirement 2), look up the selected ingredient's `Primary Supplier ID` in the Vendor Contacts table and display that supplier's email and lead time alongside the ingredient detail.

*Hint:* Use `df.loc[df["Supplier ID"] == supplier_id]` to filter the vendor table.

### Requirement 4 — Code Quality (2 pts)

- No duplicate `pd.read_csv()` calls for the same file (load each file once at the top)
- App runs without errors
- Code is committed to GitHub with a meaningful commit message

---

## Submission

1. Push your final `app.py` to your GitHub repo
2. Submit the GitHub link on Canvas

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Vendor tab with filter and metric | 3 |
| Ingredient detail view | 3 |
| Supplier lookup linked to ingredient | 2 |
| Code quality and GitHub commit | 2 |
| **Total** | **10** |
