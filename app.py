import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌦️ Live Weather App")

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if not city:
        st.error("Please enter a city name.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            st.success(f"Weather in {city.title()}")

            st.write(f"**Temperature:** {data['main']['temp']}°C")
            st.write(f"**Feels Like:** {data['main']['feels_like']}°C")
            st.write(f"**Condition:** {data['weather'][0]['description'].title()}")
            st.write(f"**Humidity:** {data['main']['humidity']}%")
            st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")

        else:
            st.error("City not found or API error.")
            st.write("Debug info:", response.text)
