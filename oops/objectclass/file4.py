
class bike:
    def __init__(self,clr,cost,brand):
        self.clr=clr
        self.cost=cost 
        self.brand=brand

    def __str__(self):
        return "strimplementation"    

    def __repr__(self):
        return f"{self.clr} {self.cost} {self.brand}"
    
b1=bike("black",20000,"RX") #instance of bike
print(b1)        

b2=bike("pink",99000,"RX") #instance of bike
print(b2)        

print(repr(b2)) #printing using collection

print("____________________________________________________________")

lob=[b1,b2]
print(lob)     #using collection
        
