class pen:
    def __init__(self):
        self.name="natraj" #iv1
        self.cost=10       #iv2

p1=pen() #instance1 pen()=constructor call  p1=reference
p2=pen() #instance2

print(p1.__dict__)
print(p2.__dict__)

print("----------------------------------------------------------")

#w parameters

class pen:
    def __init__(self,name,cost):
        self.name = name #iv1
        self.cost = cost      #iv2

p1=pen("doms",10) #instance1 pen()=constructor call  p1=reference
p2=pen("apsara",16) #instance2

print(p1.__dict__)
print(p2.__dict__)

#create friend instance w name loc and school

class Friend:
    def __init__(self,name,loc,school):
        self.name = name #iv1
        self.loc = loc      #iv2
        self.school = school

f1=Friend("chandu","blr","vgs") #instance1 pen()=constructor call  p1=reference
f2=Friend("madhu","coorg","fhps") #instance2
f3=Friend("kavya","pune","agps")

print(f1.__dict__)
print(f2.__dict__)
print(f3.__dict__)