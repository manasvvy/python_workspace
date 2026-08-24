from api.weather import WeatherAPI
from random import randint

class AccuWeather(WeatherAPI):
    def acess_temp(self):
        return randint(4, 25)

    def acess_humidity(self):
        return randint(0, 100)