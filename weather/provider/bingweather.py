from api.weather import WeatherAPI
from random import randint

class Bingweather(WeatherAPI):
    def acess_temp(self):
        return randint(11, 36) 

    def acess_humidity(self):
        return randint(0, 100)
