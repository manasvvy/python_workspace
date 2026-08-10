#EX1
class vehicle:
    def move(self):
        print("vehicle moves")

class bike(vehicle):
    def ride(self):
        print("ride a bike")   

class electiricbike(bike):
    def charge(self):
        print("it needs charge")             

v=vehicle()
v.move()
print(vehicle.__dict__) 

b=bike()
b.ride()
print(bike.__dict__)

e=electiricbike()
e.charge()
print(electiricbike.__dict__) 
______________________________________________________________________________________________________________________________________________
#EX2

class employee:
    def work(self):
        print("employee works")

class dev(employee):
    def develop(self):
        print("developer develops")   

class fde(dev):
    def design(self):
        print("ui/ux design")             

e=employee()
e.work()
print(employee.__dict__)

d=dev()
d.develop()
print(dev.__dict__)

f=fde()
f.design()
print(fde.__dict__)
