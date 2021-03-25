import requests
from .apikeys import ZIP_CODE, WEATHER_API_KEY

def get_temp():
    weather_info = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE}&appid={WEATHER_API_KEY}').json()
    kelvin_temp = float(weather_info['main']['temp'])
    return int((kelvin_temp - 273.15)* ( 9 / 5 ) + 32)
