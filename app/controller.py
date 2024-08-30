import requests
from datetime import datetime, timedelta
from database import get_data_from_db, clear_db
from init_db import initDB


def degrees_to_direction(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / 22.5) % 16
    return directions[index]


def fetch_weather_data():
    initDB()
    latitude = 55.7558  # Широта для Москвы
    longitude = 37.6173  # Долгота для Москвы
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,"\
          f"temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_sum,wind_speed_10m_max,"\
          f"wind_gusts_10m_max,wind_direction_10m_dominant,sunrise,sunset&timezone=Europe%2FMoscow&" \
          f"start_date={start_date}&end_date={end_date}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
