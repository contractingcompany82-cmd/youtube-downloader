import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌦️ Live Weather App")

API_KEY = st.secrets["OPENWEATHER_API_KEY"]  # Store API key safely in Streamlit Cloud

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if city.strip() == "":
        st.error("Please enter a valid city name.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            desc = data["weather"][0]["description"].title()

            st.success(f"Weather in {city.title()}")

            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Feels Like:** {feels}°C")
            st.write(f"**Condition:** {desc}")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind} m/s")

        else:
            st.error("City not found or API error.")
