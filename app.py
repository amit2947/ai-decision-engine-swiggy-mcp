import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Food Decision Assistant", layout="wide")

# =========================
# LOGIN (FAKE OTP)
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "otp" not in st.session_state:
    st.session_state.otp = None

# LOGIN SCREEN
if not st.session_state.logged_in:

    st.title("🔐 Login with Mobile OTP (Demo)")

    # 👉 Guest login
    if st.button("🚀 Continue as Guest"):
        st.session_state.logged_in = True
        st.rerun()

    st.divider()
    st.markdown("### Or login with OTP")

    phone = st.text_input("Enter Mobile Number")

    if st.button("Send OTP"):
        if phone:
            st.session_state.otp = str(random.randint(1000, 9999))
            st.success(f"Demo OTP: {st.session_state.otp}")
        else:
            st.warning("Enter mobile number")

    entered = st.text_input("Enter OTP")

    if st.button("Verify OTP"):
        if entered == st.session_state.otp:
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Wrong OTP")

    st.stop()   # ✅ VERY IMPORTANT

# =========================
# DATA
# =========================
data = pd.DataFrame([
    {"name": "Spice Villa", "price": 500, "rating": 4.5, "time": 25, "cuisine": "north indian"},
    {"name": "Biryani House", "price": 400, "rating": 4.4, "time": 30, "cuisine": "biryani"},
    {"name": "South Express", "price": 300, "rating": 4.2, "time": 20, "cuisine": "south indian"},
    {"name": "Pizza Hub", "price": 500, "rating": 4.3, "time": 25, "cuisine": "italian"},
    {"name": "Pasta Palace", "price": 650, "rating": 4.6, "time": 30, "cuisine": "italian"},
    {"name": "Dragon Wok", "price": 350, "rating": 4.1, "time": 20, "cuisine": "chinese"},
    {"name": "Burger Point", "price": 250, "rating": 4.0, "time": 15, "cuisine": "fast food"},
])

# =========================
# DETECT CUISINE
# =========================
def detect_cuisine(text):
    text = text.lower()

    mapping = {
        "north indian": ["north indian", "punjabi"],
        "chinese": ["chinese"],
        "italian": ["italian", "pizza", "pasta"],
        "biryani": ["biryani"],
        "south indian": ["dosa", "idli", "south indian"],
        "fast food": ["burger", "fast"]
    }

    for cuisine, keywords in mapping.items():
        for k in keywords:
            if k in text:
                return cuisine

    return "any"

# =========================
# WEIGHTS
# =========================
def compute_weights(text, budget):
    text = text.lower()

    cost, quality, delivery = 0.33, 0.33, 0.33

    if "cheap" in text:
        cost += 0.4
    if "premium" in text or "best" in text:
        quality += 0.4
    if "fast" in text:
        delivery += 0.4

    if budget < 300:
        cost += 0.5
    elif budget > 600:
        quality += 0.4
        cost -= 0.2

    total = cost + quality + delivery
    return cost/total, quality/total, delivery/total

# =========================
# SCORE
# =========================
def score(df, wc, wq, wd, budget):
    df = df.copy()

    df["cost_score"] = 1 - (df["price"] / (budget + 1))
    df["quality_score"] = df["rating"] / 5
    df["delivery_score"] = 1 - (df["time"] / 60)

    df["final"] = wc*df["cost_score"] + wq*df["quality_score"] + wd*df["delivery_score"]

    return df.sort_values(by="final", ascending=False)

# =========================
# UI
# =========================
st.title("🍽️ AI Food Decision Assistant")

query = st.text_input("Describe your craving", "premium fast italian")
budget = st.slider("💰 Budget for two (₹)", 100, 1000, 500)

st.info("""
cheap → cost  
premium/best → quality  
fast → delivery  

Supported cuisines: North Indian, Chinese, Italian, Biryani, South Indian, Fast Food
""")

# =========================
# RUN
# =========================
if st.button("🍴 Get Recommendations"):

    cuisine = detect_cuisine(query)
    wc, wq, wd = compute_weights(query, budget)

    st.success(f"Cost: {round(wc,2)} | Quality: {round(wq,2)} | Delivery: {round(wd,2)}")
    st.write(f"Cuisine: {cuisine}")

    filtered = data if cuisine == "any" else data[data["cuisine"] == cuisine]

    if filtered.empty:
        st.warning("No exact cuisine match → showing all options")
        filtered = data

    ranked = score(filtered, wc, wq, wd, budget)

    st.subheader("🏆 Top Picks")

    for _, row in ranked.head(3).iterrows():
        st.markdown(f"### {row['name']}")
        st.write(f"⭐ {row['rating']} | 🚀 {row['time']} mins | 💰 ₹{row['price']} for two")

        st.write(f"""
✔ Cuisine match: {row['cuisine']}  
✔ Quality score aligns with rating {row['rating']}  
✔ Fits budget ₹{budget}  
✔ Delivery time {row['time']} mins  
""")