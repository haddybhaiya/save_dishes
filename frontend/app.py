import streamlit as st
import requests
import datetime

API_URL = "https://save-dishes-api.onrender.com/predict"

st.set_page_config(page_title="SaveDishes", layout="centered")

st.title("🍽️ SaveDishes")
st.subheader("Predict food waste and reduce it")

st.markdown("---")

# ---------- INPUTS ----------
staff_experience = st.selectbox(
    "Staff Experience",
    ["experienced", "intermediate", "new"]
)

waste_category = st.selectbox(
    "Waste Category",
    ["veg", "non-veg", "mixed"]
)

date = st.date_input("Date", datetime.date.today())

day_of_week = date.weekday()

temperature_C = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=30.0)
humidity_percent = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)

kitchen_staff = st.number_input("Kitchen Staff Count", min_value=1, value=5)
meals_served = st.number_input("Meals Served", min_value=1, value=100)
past_waste_kg = st.number_input("Past Waste (kg)", min_value=0.0, value=20.0)

special_event = st.selectbox("Special Event?", [0, 1])

# ---------- PREDICT ----------
if st.button("🔮 Predict Food Waste"):
    payload = {
        "staff_experience": staff_experience,
        "waste_category": waste_category,
        "day_of_week": day_of_week,
        "date": str(date),
        "temperature_C": temperature_C,
        "humidity_percent": humidity_percent,
        "kitchen_staff": kitchen_staff,
        "meals_served": meals_served,
        "past_waste_kg": past_waste_kg,
        "special_event": special_event
    }

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"📉 Estimated Food Waste: **{result['predicted_food_waste_kg']} kg**")
    else:
        st.error("❌ Prediction failed. Check API.")
