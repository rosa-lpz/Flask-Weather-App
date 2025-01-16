import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# Access API_KEY from .env
load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int
    temperature_min: int
    temperature_max: int
    pressure: int
    humidity: int



def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={10}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon
    


def get_current_weather(lat, lon, API_key):
    resp=requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        # From a list
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        # From main dictionary
        temperature=int(resp.get('main').get('temp')),
        temperature_min=int(resp.get('main').get('temp_min')),
        temperature_max=int(resp.get('main').get('temp_max')),
        pressure=int(resp.get('main').get('pressure')),
        humidity=int(resp.get('main').get('humidity'))

    )
    return data


def main(city_name, state_code, country_name):
    lat, lon = get_lat_lon(city_name, state_code, country_name,api_key)
    weather_data=get_current_weather(lat, lon, api_key)
    return weather_data



if __name__== "__main__":
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada',api_key)
    print(get_current_weather(lat, lon, api_key))