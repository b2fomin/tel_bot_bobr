import requests
from bs4 import BeautifulSoup
from pyowm import OWM

# Функция для получения курса валюты
def get_weather_data(town):

    owm = OWM("b1dd5e9c1a94f3e217fc42f05c461ff6")
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(town + ",RU")
        weather = observation.weather
    except:
        return False, None
    return True, {
        'detailed_status': weather.detailed_status,
        'temp': weather.temperature('celsius')['temp'],
        'humidity': weather.humidity
    }