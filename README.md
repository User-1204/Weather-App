# Weather App

## Overview

This project is a modular, GUI-based weather application built in Python. Users can enter a city manually or automatically detect their location using IP-based geolocation. The app retrieves real-time weather data and short-term forecasts from the Tomorrow.io API and presents them in a clean, user-friendly interface. Key features include dynamic weather icons, hourly and daily forecasts, and the option to toggle between Celsius and Fahrenheit. The project focuses on usability, modular code structure, and clear visual feedback to enhance the user experience.


## Features

* Enter a city manually or detect location automatically
* View real-time temperature, humidity, wind speed, and condition description
* See next 3 hours of hourly forecast and next 3 days of daily forecast
* Toggle between Celsius and Fahrenheit units
* Weather icons loaded dynamically based on weather codes
* Gradient background for improved visual appeal
* Clear input validation and error messages
* Modular code with separate GUI and logic files
* Shortcut: pressing **Enter** triggers weather update


## Theory and Concepts

### API Integration

The app uses the [Tomorrow.io Weather API](https://www.tomorrow.io/) to fetch:

* Current temperature, humidity, wind speed
* Weather condition codes
* Hourly and daily forecast data

Responses are in JSON format, which the app parses to display readable data.

### GUI Design

Built with Tkinter, the interface includes:

* Entry box for city name
* Buttons for:

  * Fetching weather
  * Detecting location
  * Toggling temperature units
* Labels to display:

  * Current weather
  * Hourly forecast
  * Daily forecast
* Weather icons loaded from the local `icons/` folder
* Gradient background created dynamically using Pillow (PIL)


### Unit Conversion

By default, the app shows Celsius. Users can toggle to Fahrenheit.
Temperature conversion uses:

```
°F = (°C × 9/5) + 32
```

A global flag (`is_celsius`) keeps track of the current unit, and temperatures update automatically.


### Weather Codes and Icons

The app maps numeric weather codes (e.g., 1000 → Clear) to human-readable descriptions.
Each weather code has a matching PNG icon stored in the `icons/` folder.


### Location Detection

For convenience, the app can detect the user’s approximate city using the [ipinfo.io](https://ipinfo.io/) API, which returns IP-based location data.


### Error Handling

The app handles:

* Empty city input
* Invalid or misspelled city names
* Missing weather icons
* API failures

Errors are displayed using message boxes to keep feedback clear and friendly.


## Project Structure

```
weather_app/
├── main.py               # Starts the app and connects GUI callbacks to logic
├── gui.py                # Defines the Tkinter interface and widgets
├── logic.py              # Handles API calls, temperature toggle, and location detection
├── codes.py              # Maps weather codes to text
├── icons/                # PNG icons named by weather code (e.g., 1000.png)
├── id.env                # Contains the Tomorrow.io API key
└── requirements.txt      # Required Python packages
```


## Technologies Used

* Python 3.x
* Tkinter (GUI)
* requests (HTTP requests)
* Pillow (PIL) for image handling
* dotenv (read API key from `.env` file)

To install dependencies:

```bash
pip install -r requirements.txt
```

Also, create an `id.env` file with:

```
API_KEY=your_tomorrow_io_key
```


## Running the Application

Run this command from the project folder:

```bash
python main.py
```

A window will open. Enter a city or click **Detect Location**, then press **Get Weather** or just hit **Enter**.


## Possible Enhancements

* Add icons for additional weather codes
* Show precipitation probability, pressure, or sunrise/sunset times
* Dark mode or theme customization
* Remember last searched location
* Display forecast charts or graphs


## Demo Video

https://www.linkedin.com/posts/sakshii125_python-internship-oasisinfobyte-activity-7354382313222250496-D6k3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFlzQCEBcgHpQxLz_XBWlVGbkhDirbT-r5Y


## GUI Preview

<img width="520" height="912" alt="Image" src="https://github.com/user-attachments/assets/91ae490e-9bf1-4037-97ce-4e247118e01a" />
