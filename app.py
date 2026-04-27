import streamlit as st
from decision_engine import recommend

st.title("AI Food Decision Assistant")

budget = st.slider("Budget (₹)", 100, 1000, 300)
priority = st.selectbox("Priority", ["cheap", "fast", "quality"])
cuisine = st.selectbox("Cuisine", ["North Indian", "Chinese", "Fast Food"])

if st.button("Get Recommendations"):
    results = recommend(budget, priority, cuisine)

    for r in results:
        st.write(f"{r['name']} | ₹{r['price']} | ⭐{r['rating']} | {r['delivery']} mins")