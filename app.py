import streamlit as st
import requests

API_KEY = "6a18383c8cb44785ddcc220e7019b233"   # <-- yahan apni key daalo
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.set_page_config(page_title="Weather App", page_icon="🌦", layout="centered")

# ---------- UI Styling ----------
st.markdown("""
    <style>
        .big-temp { font-size: 60px; font-weight: 700; text-align: center; }
        .weather-box {
            padding: 20px;
            border-radius: 15px;
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Weather Fetch Function ----------
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        r = requests.get(BASE_URL, params=params, timeout=10)
        data = r.json()
        if r.status_code != 200:
            return None, data.get("message", "Error")
        return data, None
    except Exception as e:
        return None, str(e)

# ---------- App UI ----------
st.title("🌦 Beautiful Weather App")
st.write("City ka naam likho aur stylish weather info dekho.")

city = st.text_input("City Name", "London")

if st.button("Check Weather"):
    data, error = get_weather(city)

    if error:
        st.error(f"⚠️ Error: {error}")
    else:
        weather = data["weather"][0]
        main = data["main"]
        wind = data["wind"]

        icon = weather["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

        st
