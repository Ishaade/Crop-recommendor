import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("crop_model.pkl", "rb"))

# Page configuration
st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="centered")

# Title and instructions
st.title("🌿 Crop Recommendation System")
st.markdown("Enter the **soil nutrients** and **environmental conditions** below to get a crop suggestion.")

# Optional: Custom CSS (styling buttons and titles only, no white box)
st.markdown("""
    <style>
    h1, .stButton>button {
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, format="%.2f")
    P = st.number_input("Phosphorus (P)", min_value=0.0, format="%.2f")
    K = st.number_input("Potassium (K)", min_value=0.0, format="%.2f")
    ph = st.number_input("Soil pH", min_value=0.0, format="%.2f")

with col2:
    temperature = st.number_input("Temperature (°C)", format="%.2f")
    humidity = st.number_input("Humidity (%)", format="%.2f")
    rainfall = st.number_input("Rainfall (mm)", format="%.2f")

if st.button("🌱 Predict Best Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop to Plant: **{prediction.capitalize()}**")
