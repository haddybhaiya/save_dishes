import streamlit as st
import requests
from datetime import date

# -------------------- CONFIG --------------------
API_URL = "https://save-dishes-api.onrender.com/predict"

st.set_page_config(
    page_title="SaveDishes • Food Waste Predictor",
    page_icon="🍽️",
    layout="centered"
)

# -------------------- HEADER --------------------
st.title("🍽️ SaveDishes")
st.subheader("Predict food waste before it happens")

st.markdown(
    """
    SaveDishes helps restaurants **reduce food waste**, **cut costs**,  
    and **make smarter preparation decisions** using machine learning.
    """
)

st.divider()

# -------------------- INPUT SECTION --------------------
st.markdown("### 🧾 Kitchen & Day Details")

col1, col2 = st.columns(2)

with col1:
    staff_experience = st.selectbox(
        "Staff Experience Level",
        ["beginner", "intermediate", "expert"]
    )

    waste_category = st.selectbox(
        "Waste Category",
        ["vegetable", "meat", "dairy", "mixed"]
    )

    day_of_week = st.selectbox(
        "Day of Week",
        options=list(range(7)),
        format_func=lambda x: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][x]
    )

with col2:
    selected_date = st.date_input(
        "Date",
        value=date.today()
    )

    temperature_C = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=30.0
    )

    humidity_percent = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

st.markdown("### 👨‍🍳 Operations Info")

col3, col4 = st.columns(2)

with col3:
    kitchen_staff = st.number_input(
        "Kitchen Staff Count",
        min_value=1,
        max_value=100,
        value=10
    )

    meals_served = st.number_input(
        "Meals Served",
        min_value=1,
        max_value=5000,
        value=200
    )

with col4:
    past_waste_kg = st.number_input(
        "Previous Day Waste (kg)",
        min_value=0.0,
        value=10.0
    )

    special_event = st.selectbox(
        "Special Event Today?",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

st.divider()

# -------------------- PREDICTION --------------------
if st.button("🔍 Predict Food Waste", use_container_width=True):
    payload = {
        "staff_experience": staff_experience,
        "waste_category": waste_category,
        "day_of_week": day_of_week,
        "date": selected_date.strftime("%Y-%m-%d"),
        "temperature_C": temperature_C,
        "humidity_percent": humidity_percent,
        "kitchen_staff": kitchen_staff,
        "meals_served": meals_served,
        "past_waste_kg": past_waste_kg,
        "special_event": special_event
    }

    with st.spinner("Analyzing kitchen patterns..."):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        prediction = response.json()["predicted_food_waste_kg"]

        st.markdown("### 📊 Prediction Result")

        st.metric(
            label="Expected Food Waste (kg)",
            value=f"{prediction}"
        )

        # Business guidance
        if prediction > 30:
            st.error("⚠️ High waste expected. Reduce food preparation and monitor inventory.")
        elif prediction > 15:
            st.warning("⚠️ Moderate waste expected. Adjust portions carefully.")
        else:
            st.success("✅ Low waste expected. Operations look efficient!")

    else:
        st.error("❌ Could not fetch prediction. Please try again later.")

# -------------------- FOOTER --------------------
st.divider()

st.markdown(
    """
    **About this project**  
    Built as an end-to-end ML system using:
    - scikit-learn (ML)
    - FastAPI + Docker (Backend)
    - Streamlit (Frontend)

    Designed for restaurants to reduce cost and environmental impact.
    """
)
