# Day 2 — In-Class Exercise: Extend the Catalog App

**Time:** ~40 minutes  
**Submission:** Push to your GitHub repo and submit the link on Canvas before leaving class.

---

## Starting Point

Use the `app.py` you built on Day 1, or start fresh with the version from [day1-intro.md](day1-intro.md).

---

## Tasks

### Task 1 — Add a Second Tab (Ingredients)

Streamlit supports tabs. Add a second tab that displays the `Ingredient_Catalog.csv` data.

```python
tab1, tab2 = st.tabs(["Products", "Ingredients"])

with tab1:
    # your products code here

with tab2:
    df_ing = pd.read_csv("data/Ingredient_Catalog.csv")
    st.dataframe(df_ing)
```

---

### Task 2 — Add a Search Box to the Ingredients Tab

Add a text input that filters the ingredients table by description:

```python
search = st.text_input("Search ingredients", "")
if search:
    df_ing = df_ing[df_ing["Description"].str.contains(search, case=False, na=False)]
```

---

### Task 3 — Show a Summary Metric

On the Products tab, display the number of products and the average retail price using `st.metric()`:

```python
col1, col2 = st.columns(2)
col1.metric("Products", len(df))
col2.metric("Avg Retail Price", f"${df['Retail Price'].mean():.2f}")
```

---

### Task 4 (Stretch) — Price Range Slider

Add a price range slider to filter products by retail price:

```python
min_p, max_p = float(df["Retail Price"].min()), float(df["Retail Price"].max())
price_range = st.sidebar.slider("Price range", min_p, max_p, (min_p, max_p))
df = df[(df["Retail Price"] >= price_range[0]) & (df["Retail Price"] <= price_range[1])]
```

---

## Submission Checklist

- [ ] App runs without errors
- [ ] Two tabs: Products and Ingredients
- [ ] Search box on Ingredients tab works
- [ ] Metrics displayed on Products tab
- [ ] Code committed and pushed to GitHub
- [ ] Canvas submission link posted
