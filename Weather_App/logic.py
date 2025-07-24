import os
import requests
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox
from codes import weather_conditions

# Global toggle for Celsius/Fahrenheit
is_celsius = True

# Format timestamp to readable time or day
def format_time(timestamp, mode="time"):
    dt = datetime.fromisoformat(timestamp[:-1])
    return dt.strftime("%I %p") if mode == "time" else dt.strftime("%a")

# Fetch and display weather for a given city
def get_weather(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY):
    global is_celsius
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Clear previous
    result_label.config(text="")
    icon_label.config(image=""); icon_label.image = None
    hourly_label.config(text="")
    daily_label.config(text="")

    try:
        # Current weather
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        res = requests.get(url); res.raise_for_status()
        v = res.json()["data"]["values"]

        temp = v["temperature"] if is_celsius else v["temperature"] * 9/5 + 32
        unit = "°C" if is_celsius else "°F"
        condition = weather_conditions.get(v["weatherCode"], "Unknown")

        text = (f"📍 {city.title()}\n\n"
                f"🌡️ Temperature: {temp:.1f}{unit}\n"
                f"💧 Humidity: {v['humidity']}%\n"
                f"💨 Wind speed: {v['windSpeed']} km/h\n"
                f"☁️ Condition: {condition}\n")
        result_label.config(text=text)

        # Load icon by weather code
        icon_file = f"{v['weatherCode']}.png"
        icon_path = os.path.join("icons", icon_file)
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((64, 64))
            icon_label.image = ImageTk.PhotoImage(img)
            icon_label.config(image=icon_label.image)
        else:
            icon_label.config(text="Icon not found")

        # Forecast data
        forecast_url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={API_KEY}"
        res = requests.get(forecast_url); res.raise_for_status()
        forecast = res.json()["timelines"]

        # Hourly (next 3)
        hourly_text = "\n🕓 Hourly Forecast:\n"
        for h in forecast["hourly"][:3]:
            t = h["values"]["temperature"]
            t = t if is_celsius else t * 9/5 + 32
            hourly_text += f"{format_time(h['time'])}: {t:.1f}{unit}\n"
        hourly_label.config(text=hourly_text)

        # Daily (next 3)
        daily_text = "\n📅 3-Day Forecast:\n"
        for d in forecast["daily"][:3]:
            tmin = d["values"]["temperatureMin"]
            tmax = d["values"]["temperatureMax"]
            if not is_celsius:
                tmin = tmin * 9/5 + 32
                tmax = tmax * 9/5 + 32
            day = format_time(d["time"], mode="day")
            daily_text += f"{day}: {tmin:.1f}{unit} - {tmax:.1f}{unit}\n"
        daily_label.config(text=daily_text)

    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Toggle between Celsius & Fahrenheit
def toggle_unit(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY):
    global is_celsius
    is_celsius = not is_celsius
    get_weather(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY)

# Detect location by IP and show weather
def detect_location(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY):
    try:
        res = requests.get("https://ipinfo.io/json"); res.raise_for_status()
        city = res.json().get("city")
        if city:
            city_entry.delete(0, "end")
            city_entry.insert(0, city)
            get_weather(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY)
        else:
            messagebox.showerror("Error", "Could not detect location.")
    except Exception as e:
        messagebox.showerror("Error", f"Location detection failed: {e}")
