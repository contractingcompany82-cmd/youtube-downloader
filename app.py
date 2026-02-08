import streamlit as st
import requests

API_KEY = "6a18383c8cb44785ddcc220e7019b233"  # yahan apna key daalo
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        data = resp.json()
        if resp.status_code != 200:
            return None, data.get("message", "Error")
        return data, None
    except Exception as e:
        return None, str(e)

st.set_page_config(page_title="Weather App", page_icon="☁️")

st.title("🌤 Simple Weather Checker")
st.write("City ka naam likho aur weather dekh lo.")

city = st.text_input("City name", value="London")

if st.button("Check Weather"):
    if not city.strip():
        st.warning("Pehle city ka naam likho.")
    else:
        with st.spinner("Weather laa raha hoon..."):
            data, error = get_weather(city.strip())

        if error:
            st.error(f"Kuch gadbad hai: {error}")
        else:
            st.success(f"Weather for {data['name']}, {data['sys']['country']}")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Temperature (°C)", f"{data['main']['temp']}°C")
                st.metric("Feels like", f"{data['main']['feels_like']}°C")
                st.write(f"**Condition:** {data['weather'][0]['description'].title()}")

            with col2:
                st.write(f"**Humidity:** {data['main']['humidity']}%")
                st.write(f"**Pressure:** {data['main']['pressure']} hPa")
                st.write(f"**Wind:** {data['wind']['speed']} m/s")

            st.write("---")
            st.json(data)  # raw response bhi dekhna ho to
