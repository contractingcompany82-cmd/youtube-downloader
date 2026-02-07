import streamlit as st
import requests

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

st.write("Testing API Key...")

url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"

response = requests.get(url)

st.write("Status Code:", response.status_code)
st.write("Response:", response.text)
