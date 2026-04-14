# Peak Fuel Foods — Data Dictionary

All CSV files live in this `data/` directory. **Do not modify the raw files** — load them read-only in your apps. If an assignment requires saving data, write to a SQLite database instead.

---

## Files Overview

| File | Rows | Used Starting |
|------|------|---------------|
| [Products___Pricing.csv](#products___pricingcsv) | 5 products | Week 1 |
| [Ingredient_Catalog.csv](#ingredient_catalogcsv) | 33 ingredients | Week 1 |
| [Vendor_Contacts___Terms.csv](#vendor_contacts___termscsv) | 24 suppliers | Homework 1 |
| [Sales_Log.csv](#sales_logcsv) | 143 transactions | Week 2 |
| [Inventory_Count.csv](#inventory_countcsv) | 33 ingredients | Homework 2 |
| [Recipes___Ingredients.csv](#recipes___ingredientscsv) | 56 BOM rows | Homework 2 |
| [PO_Tracker.csv](#po_trackercsv) | 46 POs | Week 3 |
| [Receiving_Log.csv](#receiving_logcsv) | 10 records | Week 3 |

---

## When to Use Each File

| Week / Assignment | Files Needed |
|-------------------|-------------|
| Week 1 | Products___Pricing.csv, Ingredient_Catalog.csv |
| Homework 1 | + Vendor_Contacts___Terms.csv |
| Week 2 | + Sales_Log.csv |
| Homework 2 | + Inventory_Count.csv, Recipes___Ingredients.csv |
| Week 3 | + PO_Tracker.csv, Receiving_Log.csv |

---

## Column Definitions

### Products___Pricing.csv

5 rows — one per finished product SKU.

| Column | Type | Description |
|--------|------|-------------|
| SKU | string | Unique product identifier (e.g., PF-WHEY-VAN) |
| Product Name | string | Marketing name of the product |
| Description | string | Short product description |
| Category | string | Product line (e.g., Protein, Pre-Workout) |
| Unit of Measure | string | How the product is sold (e.g., bag, tub) |
| Retail Price | float | Suggested retail price in USD |

---

### Ingredient_Catalog.csv

33 rows — one per raw material or component.

| Column | Type | Description |
|--------|------|-------------|
| Ingredient SKU | string | Unique ingredient identifier |
| Description | string | Ingredient name and spec |
| Order Unit | string | Unit in which this ingredient is purchased |
| Cost Per Unit | float | Cost in USD per order unit |
| MOQ | float | Minimum order quantity |
| Primary Supplier ID | string | Supplier ID from Vendor_Contacts___Terms.csv |
| Primary Supplier Name | string | Supplier company name |

---

### Vendor_Contacts___Terms.csv

24 rows — one per supplier.

| Column | Type | Description |
|--------|------|-------------|
| Supplier ID | string | Unique supplier identifier |
| Company Name | string | Supplier's business name |
| Contact Person | string | Primary contact name |
| Email | string | Contact email |
| Phone | string | Contact phone number |
| Lead Time (weeks) | integer | Typical lead time from order to delivery |
| Payment Terms | string | e.g., Net 30, Net 15 |
| Notes | string | Any special terms or notes |

---

### Sales_Log.csv

143 rows — one per sales transaction.

| Column | Type | Description |
|--------|------|-------------|
| Date | date | Transaction date (YYYY-MM-DD) |
| Customer | string | Customer or retailer name |
| Product SKU | string | References Products___Pricing.csv |
| Product Name | string | Product display name |
| Quantity | integer | Units sold |
| Unit Price | float | Actual selling price (may differ from retail) |
| Channel | string | Sales channel (e.g., Direct, Wholesale, Online) |

---

### Inventory_Count.csv

33 rows — one per ingredient, matching Ingredient_Catalog.csv.

| Column | Type | Description |
|--------|------|-------------|
| Ingredient SKU | string | References Ingredient_Catalog.csv |
| Description | string | Ingredient name |
| On Hand Qty | float | Current quantity in stock |
| Unit | string | Unit of measure for on-hand quantity |
| Count Date | date | Date the physical count was taken |
| Location | string | Warehouse location or bin |
| Notes | string | Any discrepancy or quality notes |

---

### Recipes___Ingredients.csv

56 rows — Bill of Materials (BOM). Multiple rows per product.

| Column | Type | Description |
|--------|------|-------------|
| Product SKU | string | Finished product; references Products___Pricing.csv |
| Product Name | string | Finished product name |
| Ingredient SKU | string | Component; references Ingredient_Catalog.csv |
| Ingredient | string | Ingredient name |
| Qty Per Unit | float | Quantity of ingredient needed per unit of finished product |
| Unit | string | Unit of measure for Qty Per Unit |
| Yield Factor | float | Efficiency factor (1.0 = no waste) |
| Notes | string | Any special handling or substitution notes |

---

### PO_Tracker.csv

46 rows — one row per purchase order line.

| Column | Type | Description |
|--------|------|-------------|
| PO Number | string | Unique PO identifier |
| Supplier ID | string | References Vendor_Contacts___Terms.csv |
| Supplier Name | string | Supplier company name |
| Ingredient SKU | string | References Ingredient_Catalog.csv |
| Ingredient | string | Ingredient name |
| Qty Ordered | float | Quantity ordered |
| Unit | string | Unit of measure |
| Unit Cost | float | Cost per unit at time of order |
| Order Date | date | Date PO was issued |
| Expected Delivery | date | Promised delivery date |
| Actual Delivery | date | Actual delivery date (blank if not yet received) |
| Status | string | Open, Received, Partial, Overdue |

---

### Receiving_Log.csv

10 rows — records of physical goods receipt.

| Column | Type | Description |
|--------|------|-------------|
| PO Number | string | References PO_Tracker.csv |
| Receipt Date | date | Date goods were received |
| Ingredient SKU | string | References Ingredient_Catalog.csv |
| Ingredient | string | Ingredient name |
| Qty Received | float | Quantity actually received |
| Qty Ordered | float | Quantity that was ordered (for comparison) |
| Discrepancy | float | Qty Received minus Qty Ordered |
| Quality Notes | string | Any quality issues noted on receipt |
