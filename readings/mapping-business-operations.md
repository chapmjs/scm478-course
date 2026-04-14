# Mapping Business Operations

*A conceptual framework for SCM 478*

---

## The Problem with Spreadsheets

Most small businesses run on spreadsheets. This is not a criticism — spreadsheets are flexible, accessible, and powerful for individual tasks. The problem arises when a business needs to *connect* those tasks.

A purchase order lives in one file. The inventory it replenishes lives in another. The sales that drove the order live in a third. When each file is maintained independently, you have data silos — accurate in isolation, misleading in combination.

The job of a supply chain analyst is to map these operations and build systems that connect them.

---

## The Four Flows

Every supply chain involves four types of flow:

1. **Materials** — physical goods moving from suppliers through production to customers
2. **Information** — data about orders, inventory levels, forecasts, and status
3. **Money** — payments flowing opposite to materials
4. **Time** — lead times, cycle times, delays, and deadlines

Most operational problems are really *information* problems. Materials are delayed because no one knew the order was late. Inventory runs out because the reorder signal was missed. A bottleneck forms because capacity data was never collected.

The systems you build in this course are fundamentally **information systems** — they make the other three flows visible and manageable.

---

## Levels of Visibility

Think of operational visibility in four levels:

| Level | Question Answered | Example |
|-------|------------------|---------|
| **Descriptive** | What happened? | Sales by product last month |
| **Diagnostic** | Why did it happen? | Which channel drove the spike? |
| **Predictive** | What will happen? | Forecast for next quarter |
| **Prescriptive** | What should we do? | Reorder X units by Friday |

You will build through all four levels across the semester, starting with descriptive dashboards in Week 1 and reaching prescriptive recommendations by Week 11.

---

## The Operations Map for Peak Fuel Foods

```
Suppliers
    ↓  [Purchase Orders]
Receiving
    ↓  [Receiving Log]
Warehouse / Inventory
    ↓  [Production Orders + BOM]
Finished Goods
    ↓  [Sales Orders]
Customers
```

Each arrow is a transaction. Each transaction generates data. Each data point belongs in a table. The tables you will work with in this course represent every major transaction in this map.

---

## From Map to Model

Once you can see the map, you can build models:

- **Shortage warning:** Compare inventory on hand against requirements from open orders
- **Demand forecast:** Use historical sales to project future needs
- **BOM explosion:** Multiply finished goods requirements by ingredient quantities
- **Constraint analysis:** Find where flow is blocked and quantify the cost

These are not abstract concepts. By Week 9, you will have built all of them for Peak Fuel Foods.

---

## Discussion Questions

1. Where in the Peak Fuel operations map do you think information problems are most likely to occur? Why?
2. Which of the four levels of visibility (descriptive, diagnostic, predictive, prescriptive) do you think is most valuable for a small manufacturer? Does your answer change for a large one?
3. What data would you want that Peak Fuel doesn't currently collect?
