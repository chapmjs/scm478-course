# Day 1 — Course Introduction and First Streamlit App

## Agenda

1. Course overview (15 min)
2. Environment check — run `python setup/self_check.py` together (10 min)
3. Live demo: a minimal Streamlit app (20 min)
4. You build it: product catalog starter (30 min)
5. Debrief and questions (10 min)

---

## Why We're Here

Supply chain analysts spend most of their time in spreadsheets. The problem: spreadsheets don't scale, don't share well, and don't update automatically. In this course you will learn to build *apps* — interactive web tools that let anyone explore supply chain data without touching a formula.

The technology stack:
- **Python** — data loading and logic
- **Pandas** — data manipulation
- **Streamlit** — turns Python scripts into web apps with almost no extra code
- **GitHub** — version control and portfolio

---

## Your First Streamlit App

Create a file called `app.py` in your personal course repo. Here is the minimum viable product for today:

```python
import streamlit as st
import pandas as pd

st.title("Peak Fuel Foods — Product Catalog")

df = pd.read_csv("data/Products___Pricing.csv")
st.dataframe(df)
```

Run it:
```bash
streamlit run app.py
```

You should see a table in your browser at `http://localhost:8501`.

---

## Adding a Filter

Extend the app to filter by category:

```python
import streamlit as st
import pandas as pd

st.title("Peak Fuel Foods — Product Catalog")

df = pd.read_csv("data/Products___Pricing.csv")

categories = ["All"] + sorted(df["Category"].unique().tolist())
selected = st.sidebar.selectbox("Category", categories)

if selected != "All":
    df = df[df["Category"] == selected]

st.dataframe(df)
st.caption(f"{len(df)} product(s) shown")
```

---

## Concepts to Know for the RAT

- What does `pd.read_csv()` return?
- What does `st.dataframe()` do vs `st.table()`?
- What is a Streamlit sidebar used for?
- How do you run a Streamlit app from the terminal?
- What is a GitHub repository?

---

## Before Next Class

1. Make sure your app runs without errors
2. Push your `app.py` to your GitHub repo
3. Read [founders-story.md](../../readings/founders-story.md)
