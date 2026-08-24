#fest stage
# from provider.accuweather import AccuWeather
# class MakeMyTrip:
#     def book_ticket(self,source,destination):
#         m=AccuWeather()#object create inside method
#         print(f"{destination} weather details")
#         print(m.acess_temp())
#         print(m.acess_humidity())
#         print(f"ticket booked from {source} to {destination}")
# m1=MakeMyTrip()
# m1.book_ticket("bengalore","pondi")    


from provider.accuweather import AccuWeather
from provider.bingweather import Bingweather
class MakeMyTrip:
    def __init__(self,sp):#custom constructor
        self.sp=sp#initializing the servicxe provider
    def book_ticket(self,source,destination):
        # m=AccuWeather()#object create inside method now its not neccesary
        print(f"{destination} weather details")
        print(self.sp.acess_temp())#using the serviece provider acess temp/humidity
        print(self.sp.acess_humidity())
        print(f"ticket booked from {source} to {destination}")
   
m1=MakeMyTrip(AccuWeather())#i have pass during object
m1.book_ticket("bengalore","pondi") 


from provider.accuweather import AccuWeather
from provider.bingweather import Bingweather
class MakeMyTrip:
    def __init__(self,sp):#custom constructor
        self.sp=sp#initializing the servicxe provider
    def book_ticket(self,source,destination):
        # m=AccuWeather()#object create inside method now its not neccesary
        print(f"{destination} weather details")
        print(self.sp.acess_temp())#using the serviece provider acess temp/humidity
        print(self.sp.acess_humidity())
        print(f"ticket booked from {source} to {destination}")
    def change_provider(self,new_provider):#to switch /change the service
        self.sp=new_provider    
m1=MakeMyTrip(AccuWeather())#i have pass during object
m1.book_ticket("bengalore","pondi")#accuweather
print("----------------")
m1.change_provider(Bingweather())#calling the method to change the service provider
m1.book_ticket("chennai","pondi")