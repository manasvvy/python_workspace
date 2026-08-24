from abc import ABC, abstractmethod

class WeatherAPI(ABC):
    @abstractmethod
    def acess_temp(self):
        pass 

    @abstractmethod
    def acess_humidity(self):
        pass
