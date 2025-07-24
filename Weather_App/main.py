import os
from dotenv import load_dotenv
import gui
import logic

load_dotenv("id.env")
API_KEY = os.getenv("API_KEY")

# Build GUI and define callbacks
city_entry, result_label, icon_label, hourly_label, daily_label, root = gui.build_gui({
    'get_weather': lambda: logic.get_weather(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY),
    'toggle_unit': lambda: logic.toggle_unit(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY),
    'detect_location': lambda: logic.detect_location(city_entry, result_label, icon_label, hourly_label, daily_label, API_KEY)
})

root.mainloop()
